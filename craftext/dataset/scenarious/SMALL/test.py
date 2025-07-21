from craftext.dataset.scenarious.jax_build_line import test as build_line_instructions
from craftext.dataset.scenarious.jax_build_square import (
    test as build_square_instructions,
)
from craftext.dataset.scenarious.jax_localization_place import (
    test as localization_place_instructions,
)
from craftext.dataset.scenarious.jax_conditional_placing import (
    test as conditional_place_instructions,
)
from craftext.dataset.scenarious.jax_conditional_achievements import (
    test as conditional_achievements_instructions,
)

# Merging 'easy' dictionaries
easy_test_parafrased = {
    **conditional_achievements_instructions.easy_test_parafrased,
}


# Merging 'easy' dictionaries
easy_test_other_paramets = {
    **conditional_achievements_instructions.easy_test_other_paramets,
}


# Merging 'medium' dictionaries
medium_test_parafrased = {
    **build_line_instructions.medium_test_parafrased,
    **build_square_instructions.medium_test_parafrased,
    **conditional_place_instructions.medium_test_parafrased,
    **conditional_achievements_instructions.medium_test_parafrased,
    **localization_place_instructions.medium_test_parafrased,
}


# Merging 'medium' dictionaries
medium_test_other_paramets = {
    **build_line_instructions.medium_test_other_paramets,
    **build_square_instructions.medium_test_other_paramets,
    **conditional_place_instructions.medium_test_other_paramets,
    **conditional_achievements_instructions.medium_test_other_paramets,
    **localization_place_instructions.medium_test_other_paramets,
}
