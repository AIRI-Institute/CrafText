
from craftext.environment.scenarious.checkers.target_state import Achievements, TargetState
from craftext.environment.craftext_constants import Achievement, Scenarios, AchievementState

def create_target_state(required=[], forbidden=[]):
    base_vector = [AchievementState.NOT_MATTER for i in range(Achievement.MAKE_IRON_SWORD + 1)]
    max_required = max(required)
    for i in range(len(base_vector)):
        if i in required:
            base_vector[i] = AchievementState.NEED_TO_ACHIEVE
        elif i in forbidden:
            base_vector[i] = AchievementState.AVOID_TO_ACHIEVE
        if i > max_required:
            base_vector[i] = AchievementState.AVOID_TO_ACHIEVE
    target_achievements = Achievements(achievement_mask=tuple(base_vector))
    return TargetState(achievements=target_achievements)

# придеться фиксить. Список все возможноых инструкций, семплируем по категориям
easy = { 
    "COLLECT_WOOD": {
        "instruction": "Collect wood.",
        "instruction_paraphrases": [
            "Harvest logs from nearby trees.",
            "Chop down some timber to gather wood.",
            "Cut a tree to obtain wooden resources.",
            "Retrieve lumber from a fallen tree.",
            "Procure wood by felling trees in the area."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD],
            forbidden=[]
        )
    },
    "PLACE_TABLE": {
        "instruction": "Place a crafting table.",
        "instruction_paraphrases": [
            "Set down a crafting bench in the area.",
            "Install a crafting workstation at your location.",
            "Position a workbench for crafting nearby.",
            "Drop a table designed for crafting tasks.",
            "Arrange a crafting station in a suitable spot."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_TABLE],
            forbidden=[]
        )
    },
    "MAKE_WOOD_PICKAXE": {
        "instruction": "Craft a wooden pickaxe.",
        "instruction_paraphrases": [
            "Assemble a mining tool made of wood.",
            "Construct a wooden pickaxe for digging.",
            "Fashion a pickaxe out of wooden parts.",
            "Carve and build a wooden mining tool.",
            "Forge a lightweight pickaxe from wood."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_PICKAXE],
            forbidden=[]
        )
    },
    "MAKE_WOOD_SWORD": {
        "instruction": "Craft a wooden sword.",
        "instruction_paraphrases": [
            "Forge a blade made from wooden materials.",
            "Carve a wooden sword for protection.",
            "Construct a simple sword using wood.",
            "Create a weapon crafted from timber.",
            "Build a wooden blade for self-defense."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_SWORD],
            forbidden=[]
        )
    }
}


medium = {}