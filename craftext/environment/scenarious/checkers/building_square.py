import jax

from jax import (
    numpy as jnp,
    lax
)
from flax.struct import dataclass
from typing import Tuple

from typing import Union
from craftext.environment.states.state import GameData
from craftext.environment.states.state_classic import GameDataClassic

from craftext.environment.scenarious.checkers.target_state import BuildSquareState
from craftext.environment.scenarious.checkers.squeres import (
    check_square_2x2, 
    check_square_3x3, 
    check_square_4x4
)
from functools import partial

@dataclass
class Carry:
    region: jax.Array
    region_size: int
    size: int

def checker_square(game_data: Union[GameDataClassic, GameData],  target_state: BuildSquareState) -> jax.Array:
    
    block_index = target_state.block_type
    radius = 10
    size = target_state.size

    return is_square_formed(game_data, block_index, radius, size)


@partial(jax.jit, static_argnames=['radius'])
def is_square_formed(game_data: Union[GameDataClassic, GameData], block_index: int, radius: int, size: int) -> jax.Array:

     # Extract the full game map and convert to a binary mask for block_index.
    game_map = game_data.states[0].map.game_map
    binary_map = (game_map == block_index).astype(jnp.int32)

    # Get the player's coordinates.
    x, y = game_data.states[0].variables.player_position

    # Compute the side length of the search region: (2 * radius + 1).
    region_size = 2 * radius + 1

    # Slice out the square region centered on the player.
    region = lax.dynamic_slice(
        binary_map,
        start_indices=(x - radius, y - radius),
        slice_sizes=(region_size, region_size)
    )  # shape [region_size, region_size]

    # Create a flat array of all cell indices in the region.
    indices = jnp.arange(region_size * region_size)

    # Initialize carry with the region and scan parameters.
    carry = Carry(region=region, region_size=region_size, size=size)

    # Scan over each cell index, testing for a square at that center.
    _, squares = lax.scan(scan_square_function, carry, indices)

    # If any scan position yields a complete square, return True.
    return jnp.any(squares)

def check_square_by_size(center: Tuple[int, int], region: jax.Array, size: int):
    i, j = center
    
    # Dispatch to the correct checker: 2×2 → index 0, 3×3 → index 1, 4×4 → index 2
    return jax.lax.switch(
        size - 2, 
        [
            lambda: check_square_2x2((i, j), region),
            lambda: check_square_3x3((i, j), region),
            lambda: check_square_4x4((i, j), region)
        ]
    )

def scan_square_function(carry: Carry, x):
    region = carry.region
    region_size = carry.region_size
    size = carry.size

    i, j = x // region_size, x % region_size
    
    # Check for a square of the requested size at this center.
    is_square = check_square_by_size(center=(i, j), region=region, size=size)
    return carry, is_square
