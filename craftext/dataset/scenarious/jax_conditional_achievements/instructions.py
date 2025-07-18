
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

easy = {
    "PLACE_FURNACE_MAKE_IRON_SWORD_NO_MAKE_IRON_PICKAXE": {
        "instruction": "Place a furnace and craft an iron sword but do not make an iron pickaxe.",
        "instruction_paraphrases": [
            "Set up a furnace and forge an iron blade, avoiding pickaxe crafting.",
            "Place a furnace and create an iron sword, refraining from making a pickaxe.",
            "Install a furnace and craft a sword from iron, ensuring no pickaxe is made.",
            "Drop a furnace and construct an iron weapon, skipping pickaxe creation.",
            "Put down a furnace and make an iron sword, avoiding the pickaxe blueprint."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_FURNACE, Achievement.MAKE_IRON_SWORD],
            forbidden=[Achievement.MAKE_IRON_PICKAXE]
        )
    },

    "DEFEAT_ZOMBIE_NO_DEFEAT_SKELETON": {
        "instruction": "Defeat a zombie but do not kill a skeleton.",
        "instruction_paraphrases": [
            "Take down a zombie and avoid fighting skeletons.",
            "Eliminate a zombie while sparing the skeletons.",
            "Destroy a zombie but refrain from attacking skeletons.",
            "Fight and defeat a zombie, leaving skeletons untouched.",
            "Vanquish a zombie while avoiding any conflict with skeletons."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE],
            forbidden=[Achievement.DEFEAT_SKELETON]
        )
    },

    "MAKE_STONE_PICKAXE_COLLECT_COAL": {
        "instruction": "Craft a stone pickaxe and collect coal.",
        "instruction_paraphrases": [
            "Forge a stone pickaxe and mine coal.",
            "Build a pickaxe from stone and harvest coal.",
            "Create a durable mining tool and extract coal deposits.",
            "Craft a stone pickaxe and gather fuel for smelting.",
            "Make a stone pickaxe and collect black ore."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.COLLECT_COAL],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_NO_MAKE_IRON_SWORD": {
        "instruction": "Please make a stone pickaxe and avoid making an iron sword.",
        "instruction_paraphrases": [
            "Kindly forge a pickaxe using stone materials and do not create an iron-blade sword.",
            "Could you create a stone tool for mining? But refrain from constructing a sword from iron.",
            "We require a stone mining tool, however, it's important to avoid the creation of an iron combat weapon.",
            "Could I ask you to construct a stone mining implement? Make sure not to produce a martial weapon from iron.",
            "It's really necessary for you to fabricate a mining apparatus from rock but critically vital not to assemble a combat tool using iron materials."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE],
            forbidden=[Achievement.MAKE_IRON_SWORD]
        )
    },

    "EAT_PLANT_NO_EAT_COW": {
        "instruction": "Eat a plant, but make sure you haven’t eaten a cow.",
        "instruction_paraphrases": [
            "Consume a plant, without having ingested a cow.",
            "Partake in the eating of greenery, but avoid consumption of any bovine creatures.",
            "Take a bite out of some flora, but steer clear of taking a bite out of a moo-moo.",
            "Feast upon plant life solely, abstaining from the consumption of beef.",
            "Get your nourishment from plants, while maintaining a distance from cow meat."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.EAT_PLANT],
            forbidden=[Achievement.EAT_COW]
        )
    },

    "PLACE_PLANT_NO_MAKE_STONE_SWORD": {
        "instruction": "Make sure you place a small tree, but don't craft a stone sword.",
        "instruction_paraphrases": [
            "I need you to plant a treeling, but avoid creating a stone blade.",
            "It's crucial for you to put down a sapling, but abstain from making a stone saber.",
            "Place a young tree in your environment but you must not form a rock weapon.",
            "Can you position a tree sprout but please don't manufacture a weapon from stone?",
            "Ensure a plantlet is positioned while making sure not to assemble a bladed stone tool."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_PLANT],
            forbidden=[Achievement.MAKE_STONE_SWORD]
        )
    },

    "WAKE_UP_DEFEAT_ZOMBIE_COLLECT_DRINK": {
        "instruction": "You must wake up. Then, you need to defeat a zombie and lastly, fetch a drink for yourself.",
        "instruction_paraphrases": [
            "Get up from your sleep first. Post that, you must confront and win over a zombie. Lastly, make sure to obtain a drink.",
            "Rise from your rest first. Following this, it's important to tackle and overcome a zombie. In the end, secure a drink for your own self.",
            "You are required to awaken initially. Subsequent to this, it's crucial to resist and triumph over a zombie. To conclude, procure a beverage.",
            "You're needed to come out of your slumber at first. Upon accomplishing this, a zombie must be encountered and defeated. Ultimately, procure a beverage for yourself.",
            "You are supposed to wake up first. Then, a zombie needs to be challenged and defeated. Finally, get hold of a beverage."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.WAKE_UP, Achievement.DEFEAT_ZOMBIE, Achievement.COLLECT_DRINK],
            forbidden=[]
        )
    },

    "NO_MAKE_IRON_SWORD_MAKE_STONE_SWORD_COLLECT_SAPLING": {
        "instruction": "Don't create an Iron Sword. You need to, however, craft a Stone Sword and gather a Sapling.",
        "instruction_paraphrases": [
            "Make sure you aren't crafting an Iron Sword. However, you need to both collect a Sapling and manufacture a Stone Sword.",
            "You must not create an Iron Sword. Still, gather a Sapling and fashion a Stone Sword.",
            "Without constructing an Iron Sword, you should still assemble a Stone Sword and obtain a Sapling.",
            "Steer clear of creating an Iron Smasher, yet definitely build a Stone Sword and gather a Shoot.",
            "Refrain from producing a Blade of Iron; still, you must create a Stone Sword and capture a Plant Bud."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_SWORD, Achievement.COLLECT_SAPLING],
            forbidden=[Achievement.MAKE_IRON_SWORD]
        )
    },

    "COLLECT_DIAMOND_COLLECT_IRON_EAT_COW": {
        "instruction": "It's essential that you collect some diamonds, gather up some iron, and feed yourself with some cow meat.",
        "instruction_paraphrases": [
            "Acquire valuable diamonds, collect an amount of iron, and make sure to eat some cow.",
            "You need to mine for both diamonds and iron, and don't forget to fill your hunger bar with beef.",
            "Gather up some precious gems and metals, specifically diamonds and iron, and replenish your food bar with some beef.",
            "You must find and collect diamonds, iron ore, and consume bovine food.",
            "Finding diamonds, collecting iron mineral deposits, and incorporating beef into your diet is crucial."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.COLLECT_IRON, Achievement.EAT_COW],
            forbidden=[]
        )
    },

    "MAKE_WOOD_PICKAXE_DEFEAT_SKELETON_ANY_ORDER": {
        "instruction": "Make a wooden axe and defeat a skeleton, but in no specific order.",
        "instruction_paraphrases": [
            "Your target is to craft a wooden pickaxe and defeat a skeleton. You can complete these tasks in any sequence.",
            "Please, take on the skeleton after or before crafting a wooden pickaxe.",
            "Your missions are to construct a wooden pickaxe and take down a skeleton. Order doesn't matter.",
            "You need to accomplish two tasks. First is to build a wood pickaxe and second is to conquer a skeleton. You are free to choose the order.",
            "Your objectives include two tasks, creating a wooden tool for chopping, specifically a pickaxe, in addition to overcoming a skeleton enemy. You're allowed to tackle them in any order."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_PICKAXE, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "COLLECT_DRINK_NO_MAKE_STONE_SWORD": {
        "instruction": "Collect a drink yet do not construct a stone sword.",
        "instruction_paraphrases": [
            "Grab any type of beverages, but avoid making a rock sword.",
            "Obtain any kind of drinkable liquid, while abstaining from stone blade production.",
            "Acquire a sort of potable yet bypass from producing stone cutter.",
            "Procure liquid meant for drinking but make sure not to forge weapon made of stone.",
            "In your journey, make sure to gather any kind of liquid for hydration, however, be cautious not to fabricate a deadly sword out of a hard mineral rock for your protection."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DRINK],
            forbidden=[Achievement.MAKE_STONE_SWORD]
        )
    },

    "COLLECT_IRON_NO_PLACE_PLANT": {
        "instruction": "Get your hands on some iron ore but make sure not to plant anything.",
        "instruction_paraphrases": [
            "Procure an iron mineral, and refrain from engaging in any horticultural activities.",
            "Your task is to accumulate the iron substance, and remember, you must abstain from executing any planting or cultivation.",
            "Acquire an iron compound ensuring that you do not contribute to planting anything.",
            "It's crucial to gather iron yet abstain from placing any flora.",
            "Initiate the collection of iron entities, but the planting of any vegetation is prohibited."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_IRON],
            forbidden=[Achievement.PLACE_PLANT]
        )
    }
}



medium = {}

hard = {}