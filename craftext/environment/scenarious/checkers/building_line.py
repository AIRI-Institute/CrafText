import jax

from jax import (
    numpy as jnp,
    lax
)

from typing import Tuple, Callable 

from typing import Union
from craftext.environment.states.state import GameData
from craftext.environment.states.state_classic import GameDataClassic

from craftext.environment.scenarious.checkers.target_state import BuildLineState
from craftext.environment.scenarious.checkers.lines import check_line_2, check_line_3, check_line_4

from flax.struct import dataclass
from functools import partial

def checker_line(game_data: Union[GameDataClassic, GameData],  target_state: BuildLineState) -> jax.Array:
    
    block_index = target_state.block_type
    radius = 10
    size = target_state.size
    check_diagonal = target_state.is_diagonal


    return is_line_formed(game_data, block_index, radius, size, check_diagonal)

@dataclass
class Carry:
    region: jax.Array
    region_size: int
    size: int
    check_diagonal: bool

@partial(jax.jit, static_argnames=['radius'])
def is_line_formed(game_data: Union[GameDataClassic, GameData], block_index: int, radius: int, length: int, check_diagonal: bool) -> jax.Array:
    
    # Extract the raw game map and convert to binary mask for the given block_index.
    game_map = game_data.states[0].map.game_map
    binary_map = (game_map == block_index).astype(jnp.int32)

    # Get player's (x, y) position.
    x, y = game_data.states[0].variables.player_position

    # Define square region side length (2*radius + 1).
    region_size = 2 * radius + 1

    # Slice out the square region around the player.
    region = lax.dynamic_slice(
        binary_map,
        start_indices=(x - radius, y - radius),
        slice_sizes=(region_size, region_size)
    )

    # Create a flat index array to scan over every cell in region.
    indices = jnp.arange(region_size * region_size)

    # Initialize carry with region data and scan parameters.
    carry = Carry(region, region_size, length, check_diagonal)

    # Scan over each index, invoking scan_line_function to test line formation.
    #    'lines' is a 1D array of booleans for each cell.
    _, lines = lax.scan(scan_line_function, carry, indices)

    # Return True if any position yields a valid line of the required length.
    return jnp.any(lines)
    return jnp.any(lines)

def check_line_by_size(center: Tuple[int, int], region: jax.Array, size: int, check_diagonal: bool) -> Callable:
    i, j = center

    # Use JAX switch to pick specialized functions for size=2,3,4.
    # Each lambda wraps the actual checker call.
    func = lax.switch(
        size - 2,  # offset index so 2→0, 3→1, 4→2
        [
            lambda: check_line_2((i, j), region, check_diagonal),
            lambda: check_line_3((i, j), region, check_diagonal),
            lambda: check_line_4((i, j), region, check_diagonal)
        ]
    )
        
    return func

def scan_line_function(carry: Carry, x):
    region = carry.region
    region_size = carry.region_size
    size = carry.size
    check_diagonal = carry.check_diagonal
    
    # Convert flat index back to 2D coordinates (i, j).
    i = x // region_size
    j = x % region_size

    # Invoke the size-based checker for this center.
    is_line = check_line_by_size((i, j), region, size, check_diagonal)
    return carry, is_line