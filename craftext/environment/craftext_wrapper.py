from typing import Any, Optional, Union

import jax
import jax.numpy as jnp
from jax import lax

from flax import struct
from gym import Wrapper

from craftext.environment.encoders.craftext_base_model_encoder import EncodeForm
from craftext.environment.encoders.craftext_distilbert_model_encoder import (
    DistilBertEncode,
)

from craftext.environment.scenarious.manager import ScenariosNoLambda

from craftext.environment.states.state import GameData
from craftext.environment.states.state_classic import GameDataClassic

from craftext.environment.scenarious.checkers.achivments import checker_acvievments
from craftext.environment.scenarious.checkers.time_constrained import (
    checker_time_placement,
)
from craftext.environment.scenarious.checkers.building_star import checker_star
from craftext.environment.scenarious.checkers.building_line import checker_line
from craftext.environment.scenarious.checkers.building_square import checker_square
from craftext.environment.scenarious.checkers.conditional import (
    checker_conditional_placement,
)
from craftext.environment.scenarious.checkers.relevant import cheker_localization
from craftext.environment.scenarious.checkers.target_state import TargetState

from craftext.environment.craftext_constants import Scenarios

import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@struct.dataclass
class TextEnvState:
    env_state: Any
    timestep: int
    instruction: Optional[jax.Array]
    idx: int
    success_rate: float
    total_success_rate: float
    environment_key: int
    rng: int
    instruction_done: bool
    checker_id: int


def generic_check(
    game_data: Union[GameData, GameDataClassic], target_state: TargetState, idx: int
) -> jnp.ndarray:
    """
    Select and execute one of several check functions based on the given index.

    Parameters
    ----------
    game_data : Union[GameData, GameDataClassic]
        The object containing the current game world state and environment parameters.
    target_state : TargetState
        A data structure specifying the target conditions (achievements, placements,
        building shapes, timing, etc.) to be checked.
    idx : int
        An integer index selecting which checker to invoke:
            0 — checker_acvievments (achievements)
            1 — checker_conditional_placement (conditional placement)
            2 — cheker_localization (localization)
            3 — checker_line (building a line)
            4 — checker_square (building a square)
            5 — checker_star (building a star)
            6 — checker_time_placement (timed placement)
            7 — checker_acvievments (achievements again)

    Returns
    -------
    jnp.ndarray
        A JAX array (boolean or float) indicating whether the selected target
        conditions are satisfied.
    """

    def ca(ts: TargetState):
        return checker_acvievments(game_data, ts.achievements)

    def cp(ts: TargetState):
        return checker_conditional_placement(game_data, ts.conditional_placing)

    def port(ts: TargetState):
        return cheker_localization(game_data, ts.Localization_placing)

    def ilf(ts: TargetState):
        return checker_line(game_data, ts.building_line)

    def isf(ts: TargetState):
        return checker_square(game_data, ts.building_square)

    def icf(ts: TargetState):
        return checker_star(game_data, ts.building_star)

    def atp(ts: TargetState):
        return checker_time_placement(game_data, ts.time_placement)

    fns = (ca, cp, port, ilf, isf, icf, atp, ca)

    return lax.switch(idx, fns, target_state)


class InstructionWrapper(Wrapper):
    def __init__(
        self,
        env,
        config_name=None,
        scenario_handler_class=ScenariosNoLambda,
        encode_model_class=DistilBertEncode,
        encode_form=EncodeForm.EMBEDDING,
    ) -> None:
        """
        Initializes the InstructionWrapper with the environment, creating EncodeModel and CrafTextScenarios.

        Parameters:
            - env: The environment to wrap. Using Base enviroment from CrafTax
            - config_name: Optional configuration name for scenarios.
            - encode_model_class: A class for the encoding model. Defaults to DistilBertEncode.
            - encode_form: The form of encoding (EMBEDDING or TOKEN). Defaults to EMBEDDING.
        """
        super().__init__(env)

        self.encode_model = encode_model_class(form_to_use=encode_form)

        # Initialize the scenario handler with the encoding model
        self.scenario_handler = scenario_handler_class(self.encode_model, config_name)
        # initial_instruction

        self.scenario_arguments = self.scenario_handler.scenario_data_jax.arguments
        self.encoded_instruction = self.scenario_handler.initial_instruction

        self.batched_ts = TargetState.stack(self.scenario_arguments)

        self.env = env
        self.steps = 0

        # Determine the environment key and state structure
        self.environment_key = self.scenario_handler.environment_key
        self.StateStructure = GameData if self.environment_key == 1 else GameDataClassic

        logging.info(
            f"Initialized Instruction Wrapper with environment key: {'GameData' if self.environment_key == 1 else 'GameDataClassic'}"
        )

        self.n_instructions = len(self.scenario_handler.scenario_data.instructions_list)

    def reset(self, _rng, env_params, instruction_idx=-1):
        """
        Resets the environment and selects a random instruction embedding or token for the new episode.
        """
        # Reset CrafTax enviroment
        # ---------------------------------------------------------------------------------- #

        obs, state = self.env.reset(_rng, env_params)

        # ---------------------------------------------------------------------------------- #

        # Select random instruction in dataset
        # ---------------------------------------------------------------------------------- #
        idx = jax.lax.cond(
            instruction_idx == -1,
            lambda: jax.random.randint(
                _rng,
                shape=(),
                minval=0,
                maxval=len(self.scenario_handler.scenario_data_jax.embeddings_list),
            ),
            lambda: instruction_idx,
        )

        instructions_emb = self.scenario_handler.scenario_data_jax.embeddings_list[idx]

        # ---------------------------------------------------------------------------------- #

        # Initialize the state with the selected instruction embedding/token and set success rates to zero
        state = TextEnvState(
            env_state=state,
            timestep=state.timestep,
            instruction=instructions_emb,
            idx=idx,
            environment_key=self.environment_key,
            success_rate=0.0,
            total_success_rate=0.0,
            rng=_rng,
            instruction_done=False,
            checker_id=self.scenario_handler.scenario_data_jax.scenario_checker[idx],
        )
        return obs, state

    def step(self, _rng, env_state, action, env_params):
        """
        Takes a step in the environment, checking if the instruction is done, updating success rate and rewards.
        """
        # call Craftax enviroment step
        # ---------------------------------------------------------------------------------- #

        obs, state, reward, done, info = self.env.step(
            _rng, env_state.env_state, action, env_params
        )

        # ---------------------------------------------------------------------------------- #

        # Obtain the game data vector for the current state and check instruction completion
        # ---------------------------------------------------------------------------------- #

        game_data_vector = self.StateStructure.from_state(
            env_state.env_state, state, action
        )

        # Get arguments fot checker by instruction in dataset
        ts = self.batched_ts.select(env_state.idx)

        instruction_done = generic_check(game_data_vector, ts, env_state.checker_id)

        # If EXPLORE mode - give craftax reward
        reward = lax.cond(
            env_state.checker_id != Scenarios.EXPLORE,
            lambda r: r / 50,
            lambda r: r,
            reward,
        )

        reward = jax.lax.cond(
            instruction_done, lambda _: reward + 1, lambda _: reward, operand=None
        )

        # Combine Game episode ends and complete instruction
        done = instruction_done | done

        # --------------------------------------------------------------------------------- #

        new_episode_sr = env_state.success_rate + jnp.float32(instruction_done)

        # Update state with the new success rates
        state = TextEnvState(
            env_state=state,
            timestep=state.timestep,
            instruction=env_state.instruction,
            idx=env_state.idx,
            environment_key=env_state.environment_key,
            success_rate=new_episode_sr * (1 - done),
            total_success_rate=env_state.total_success_rate * (1 - done)
            + new_episode_sr * done,
            rng=env_state.rng,
            instruction_done=instruction_done,
            checker_id=env_state.checker_id,
        )

        # Update step information in info dictionary
        info.update({"SR": state.total_success_rate, "steps": self.steps})
        self.steps += 1
        return obs, state, reward, done, info


class InstructionDoneActionWrapper(InstructionWrapper):
    def __init__(
        self,
        env,
        config_name=None,
        scenario_handler_class=ScenariosNoLambda,
        encode_model_class=DistilBertEncode,
        encode_form=EncodeForm.EMBEDDING,
    ) -> None:
        super().__init__(
            env=env,
            config_name=config_name,
            scenario_handler_class=scenario_handler_class,
            encode_model_class=encode_model_class,
            encode_form=encode_form,
        )
        
        self.skip_action_id = 18

    def step(self, _rng, env_state, action, env_params):

        is_skip_action = action == self.skip_action_id

        action_for_env = jax.lax.cond(is_skip_action, lambda: 0, lambda: action)

        obs, state, reward, done, info = self.env.step(
            _rng, env_state.env_state, action_for_env, env_params
        )

        game_data_vector = self.StateStructure.from_state(
            env_state.env_state, state, action
        )

        ts = self.batched_ts.select(env_state.idx)

        instruction_done = generic_check(game_data_vector, ts, env_state.checker_id)

        reward = lax.cond(
            env_state.checker_id != Scenarios.EXPLORE,
            lambda r: r / 50,
            lambda r: r,
            reward,
        )

        reward = jax.lax.cond(
            jnp.logical_and(instruction_done, is_skip_action),
            lambda r: r + 1,
            lambda r: r,
            operand=reward,
        )

        done = jnp.logical_or(jnp.logical_and(instruction_done, is_skip_action), done)

        new_episode_sr = env_state.success_rate + jnp.float32(
            instruction_done & is_skip_action
        )

        state = TextEnvState(
            env_state=state,
            timestep=state.timestep,
            instruction=env_state.instruction,
            idx=env_state.idx,
            environment_key=env_state.environment_key,
            success_rate=new_episode_sr * (1 - done),
            total_success_rate=env_state.total_success_rate * (1 - done)
            + new_episode_sr * done,
            rng=env_state.rng,
            instruction_done=instruction_done,
            checker_id=env_state.checker_id,
        )

        info.update({"SR": state.total_success_rate, "steps": self.steps})
        self.steps += 1
        return obs, state, reward, done, info

