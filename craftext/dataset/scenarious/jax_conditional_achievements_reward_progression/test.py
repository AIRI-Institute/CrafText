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


easy_test_paraphrased = {
    "EAT_COW_MAKE_STONE_PICKAXE": {
        "instruction": "Eat a cow and craft a stone pickaxe.",
        "instruction_paraphrases": [
            "Consume beef and craft a stone pickaxe.",
            "Eat steak and forge a stone pickaxe.",
            "Devour cow meat and create a stone pickaxe.",
            "Savor a meal of beef and assemble a stone pickaxe.",
            "Enjoy cooked cow meat and build a stone pickaxe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.EAT_COW, Achievement.MAKE_STONE_PICKAXE],
            forbidden=[]
        )
    },

    "PLACE_PLANT_DEFEAT_ZOMBIE": {
        "instruction": "Place a plant and defeat a zombie.",
        "instruction_paraphrases": [
            "Plant a tree and eliminate a zombie.",
            "Place a shrub and take down a zombie.",
            "Set greenery into the ground and destroy a zombie.",
            "Drop a sapling and vanquish a zombie.",
            "Position a flower and defeat an undead creature."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_PLANT, Achievement.DEFEAT_ZOMBIE],
            forbidden=[]
        )
    },

    "PLACE_FURNACE_MAKE_IRON_SWORD_NO_MAKE_IRON_PICKAXE": {
        "instruction": "Place a furnace and craft an iron sword but do not make an iron pickaxe.",
        "instruction_paraphrases": [
            "Set up a smelter and forge an iron sword, avoiding a pickaxe.",
            "Place a heater and craft an iron blade without making a pickaxe.",
            "Install a forge and create a sword from iron, skipping pickaxe crafting.",
            "Drop a furnace and construct an iron weapon, avoiding a pickaxe.",
            "Put down a stove and make an iron sword, steering clear of pickaxe production."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_FURNACE, Achievement.MAKE_IRON_SWORD],
            forbidden=[Achievement.MAKE_IRON_PICKAXE]
        )
    },

    "DEFEAT_ZOMBIE_NOT_DEFEAT_SKELETON": {
        "instruction": "Defeat a zombie but do not kill a skeleton.",
        "instruction_paraphrases": [
            "Eliminate a walker and avoid harming skeletons.",
            "Take down an undead and spare the bone warriors.",
            "Destroy a zombie while leaving skeletons intact.",
            "Vanquish a corpse walker and refrain from attacking skeletons.",
            "Fight and defeat a ghoul, avoiding skeletons."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE],
            forbidden=[Achievement.DEFEAT_SKELETON]
        )
    },

    "MAKE_STONE_SWORD_DEFEAT_SKELETON": {
        "instruction": "Craft a stone sword and defeat a skeleton.",
        "instruction_paraphrases": [
            "Create a blade from cobblestone and slay a skeleton.",
            "Forge a stone weapon and eliminate a skeletal foe.",
            "Build a sword from rock and destroy a skeleton.",
            "Make a stone sabre and take down a skeleton.",
            "Construct a stone blade and vanquish a bony warrior."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_SWORD, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_COLLECT_COAL": {
        "instruction": "Craft a stone pickaxe and collect coal.",
        "instruction_paraphrases": [
            "Forge a mining tool from stone and mine charcoal.",
            "Build a cobblestone pickaxe and extract black ore.",
            "Create a stone tool and gather coal resources.",
            "Craft a rocky pickaxe and collect fuel ore.",
            "Make a durable pickaxe from stone and harvest coal."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.COLLECT_COAL],
            forbidden=[]
        )
    },

    "COLLECT_SAPLING_AND_IRON": {
        "instruction": "Collect a sapling and some iron in the game.",
        "instruction_paraphrases": [
            "Grab a sapling and acquire some iron while you're playing.",
            "When you are in-game, be sure to gather a sapling and some iron.",
            "Ensure you have obtained a sapling and iron in your possession during the gameplay.",
            "During your course of play, it's crucial to pick up a sapling, and don't forget to collect some iron as well.",
            "While engaging in the game, it's of utmost importance to procure a sapling and subsequently amass some iron."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_SAPLING, Achievement.COLLECT_IRON],
            forbidden=[]
        )
    },

    "EAT_PLANT_NO_EAT_COW": {
        "instruction": "Please consume a plant, while making sure that you have not ingested a cow.",
        "instruction_paraphrases": [
            "Could you devour some green vegetation? Remember, you mustn't have eaten any bovine creature.",
            "Absorb nutrients from a herb, on one condition - that you've refrained from partaking of any cow meat.",
            "I'd like you to eat a plant. But never should you have dined on a cow.",
            "Make sure to consume some plant life, given that you have not indulged in beef.",
            "You ought to be consuming vegetation, provided that beef was not included in your diet."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.EAT_PLANT],
            forbidden=[Achievement.EAT_COW]
        )
    },

    "WAKE_UP_COLLECT_WOOD_PLACE_STONE": {
        "instruction": "Start by waking up, then gather some wood, and finally place a stone.",
        "instruction_paraphrases": [
            "Awake first, collect some timber and lastly place a boulder.",
            "Begin with awakening, proceed with lumber collection, and conclude with rocky placement.",
            "First, rise from sleep, then amass a pile of logs, and in the end place a rock.",
            "Initiate with a wake-up, continue by harvesting wood, wrap up with setting down a piece of stone.",
            "Commence by stirring from slumber, accumulate wood pieces—next, finish off with a rock placement."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.WAKE_UP, Achievement.COLLECT_WOOD, Achievement.PLACE_STONE],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_PLACE_STONE_MAKE_STONE_PICKAXE": {
        "instruction": "Collect some logs, place a boulder and craft a stone pickaxe.",
        "instruction_paraphrases": [
            "Grab some timber, put down a pebble and manufacture a stone axe.",
            "Amass some firewood, set a rock and assemble a stone pick.",
            "Procure some lumber, position a stone and fabricate a stone cutter.",
            "Accumulate wood material, position a cobblestone and construct an axe made of stone.",
            "Get together blocks of wood, install a piece of rock and put together a miner's tool made of stone."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.PLACE_STONE, Achievement.MAKE_STONE_PICKAXE],
            forbidden=[]
        )
    },

    "PLACE_FURNACE_MAKE_IRON_SWORD_NO_MAKE_IRON_PICKAXE_DUPLICATE": {
        "instruction": "Place a furnace and make an iron sword. Do not make an iron pickaxe.",
        "instruction_paraphrases": [
            "Please set down a stove and forge an iron weapon, but don't create an iron mining tool.",
            "Can you establish a heating device then construct a sword made of iron? But refrain from producing an iron tool for digging.",
            "You are tasked to install a furnace and fabricate a weaponry made of iron, however, manufacturing an iron pick is not advisable.",
            "It is required of you to position a melting device properly, subsequently create a bladed weapon using iron, yet, an absolute prohibition on the creation of an excavating tool made of iron is imposed.",
            "In this quest, you are to effectuate a successful placement of a kiln and produce a defensive instrument composed mainly of iron. However, making a hand-held mining instrument out of iron is strictly prohibited."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_FURNACE, Achievement.MAKE_IRON_SWORD],
            forbidden=[Achievement.MAKE_IRON_PICKAXE]
        )
    },

    "PLACE_SAPLING_NO_MAKE_STONE_SWORD": {
        "instruction": "Ensure that you plant a sapling, but don't create a stone sword.",
        "instruction_paraphrases": [
            "I want you to place a seedling but refrain from forging a sword made of stone.",
            "Your task is to plant a sapling, while avoiding the creation of a stone-bladed weapon.",
            "Make sure to cultivate a tree sprout but do not manufacture a fighting tool crafted from rock.",
            "Your responsibility is to cultivate a small tree, and ensure you do not fashion a weapon from stone.",
            "It is crucial you plant a diminutive tree and take pains to avoid producing a lethal implement from stone."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_SAPLING],
            forbidden=[Achievement.MAKE_STONE_SWORD]
        )
    },

    "COLLECT_DRINK_PLACE_PLANT_DEFEAT_SKELETON": {
        "instruction": "Collect a beverage, place some flora, and then defeat a skeleton.",
        "instruction_paraphrases": [
            "Gather a drink, grow a plant and conquer a skeleton.",
            "Procure a liquid refreshment, set down a vegetation and eradicate a skeleton.",
            "Amass a beverage, position a sprout, and vanquish a bony figure.",
            "Accumulate a potable, fix a sapling and triumph over a skeletal adversary.",
            "Acquire an ingestible fluid, establish a shrubbery and outdo a boney antagonist."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DRINK, Achievement.PLACE_PLANT, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_DEFEAT_ZOMBIE": {
        "instruction": "Gather some timber and then vanquish a zombie.",
        "instruction_paraphrases": [
            "Collect a bit of wood and afterward eliminate a zombie.",
            "Assemble logs then defeat a living dead.",
            "Amass some lumber and subsequently slay a ghoul.",
            "Accumulate chunks of trees and next crush a monster.",
            "Round up some wooden material and subsequently conquer the undead."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.DEFEAT_ZOMBIE],
            forbidden=[]
        )
    },

    "WAKE_UP_DEFEAT_ZOMBIE_COLLECT_DRINK": {
        "instruction": "You must wake up. Then, you need to defeat a zombie and lastly, fetch a drink for yourself.",
        "instruction_paraphrases": [
            "First, you have to get out of bed. After that, go defeat a zombie. Finally, go acquire a drink.",
            "Your first task is to wake up. Once you have done that, your next job is to destroy a zombie. After that is completed, obtain a beverage for your consumption.",
            "Let's start by getting up from sleep. The next thing on your list is to handle a zombie. Finish up by getting yourself something to drink.",
            "Wake up from your slumber first, then take on a zombie. After you have accomplished those tasks, find a drink for yourself.",
            "Your journey begins when you awaken. After that, go ahead and confront a zombie. End your journey with securing a drink."
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
            "Avoid making an Iron Sword, but be sure to forge a Stone Blade and pick up a Sprout.",
            "Without constructing an Iron Smasher, you should still assemble a Pebble Cutter and obtain a Seedling.",
            "Make sure not to form an Iron Saber, yet definitely build a Boulder Slicer and accumulate a Seed.",
            "Steer clear of creating a Sword of Iron, yet it's crucial to manufacture a Rock Slicer and gather a Shoot.",
            "Refrain from producing a Blade of Iron; still, you must create a Sword out of Stone and capture a Plant Bud."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_SWORD, Achievement.COLLECT_SAPLING],
            forbidden=[Achievement.MAKE_IRON_SWORD]
        )
    },

    "COLLECT_IRON_MAKE_WOOD_PICKAXE_DEFEAT_SKELETON": {
        "instruction": "Gather some iron, make a wooden pickaxe and defeat a skeleton.",
        "instruction_paraphrases": [
            "Find some iron ore, craft a wooden pickaxe and vanquish a skeleton.",
            "Get hold of some iron, fabricate a pickaxe of wood and conquer a skeleton enemy.",
            "Accumulate some iron, construct a pickaxe made of wood and obliterate a skeleton.",
            "Procure some iron resources, build a wooden tool called pickaxe and eliminate a skeletal adversary.",
            "Requisition some iron mineral, engineer a pickaxe utilizing wood and triumph over a bony antagonist."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_IRON, Achievement.MAKE_WOOD_PICKAXE, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_AND_STONE": {
        "instruction": "Collect both wood and stone in the game.",
        "instruction_paraphrases": [
            "Gather wood and stone resources in your gameplay.",
            "During your game, ensure you have gathered both timber and rocks.",
            "Make sure to collect resources like lumber and boulders while playing game.",
            "In the game, accumulate timberwood items and stone elements.",
            "Carry out an action to collect both woody materials and stoneworks during your game session."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.COLLECT_STONE],
            forbidden=[]
        )
    },

    "MAKE_WOOD_SWORD_PLACE_PLANT": {
        "instruction": "Craft a wooden sword and cultivate a plant.",
        "instruction_paraphrases": [
            "Make a wooden sword and grow a plant.",
            "Fabricate a timber sword and breed a plant.",
            "Manufacture an arboreal blade and plant a seedling.",
            "Construct a lumber broadsword and develop some vegetation.",
            "Create a wooden cutting edge weapon and nurture a botanical specimen."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_SWORD, Achievement.PLACE_PLANT],
            forbidden=[]
        )
    },

    "COLLECT_STONE_MAKE_IRON_SWORD": {
        "instruction": "Please gather rock and then make an iron sword.",
        "instruction_paraphrases": [
            "Collect some stone first and then forge a sword made of iron.",
            "Could you acquire some pebbles first and afterwards create an iron blade?",
            "Initially amass some rock material and subsequently construct a weapon with iron.",
            "I would appreciate if you could gather boulders initially, following by the task of forming a sword using iron.",
            "Is it possible for you to initially accumulate some stone and subsequently proceed with the forging of a weapon made from iron?"
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_STONE, Achievement.MAKE_IRON_SWORD],
            forbidden=[]
        )
    },

    "COLLECT_DIAMOND_COLLECT_IRON_EAT_COW": {
        "instruction": "It's essential that you collect some diamonds, gather up some iron, and feed yourself with some cow meat.",
        "instruction_paraphrases": [
            "Don't forget to mine some diamonds, gather a few iron ores and eat the meat of a cow.",
            "To survive, make sure you mine diamonds, collect iron ores, and also eat beef.",
            "You need to look out for diamonds to mine, collect some iron and of course, feed on cattle meat.",
            "It's vital that you mine some precious diamonds, search for and gather iron ores around, also remember you'll need to eat beef to nourish yourself.",
            "You'll need to ensure that you heavily mine a lot of diamond ores, engage in serious searches for iron ores and also, partake in feeding on the succulent flesh of cows."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.COLLECT_IRON, Achievement.EAT_COW],
            forbidden=[]
        )
    },

    "MAKE_WOOD_PICKAXE_DEFEAT_SKELETON": {
        "instruction": "Create an axe made of wood and defeat a bony monster.",
        "instruction_paraphrases": [
            "Conquer a skeleton after crafting a timber hatchet.",
            "Vanquish a bone creature post manufacturing a lumber splitting tool.",
            "Overcome a skeletal adversary subsequent to the fabrication of a log splitter.",
            "Triumph over an osteal opponent following the development of a woodcutter's implement.",
            "Subjugate an exoskeletal entity subsequent to the production of a timber chopper."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_PICKAXE, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "DEFEAT_ZOMBIE_EAT_PLANT": {
        "instruction": "Defeat a zombie and then eat a plant.",
        "instruction_paraphrases": [
            "Take down an undead monster and consume some flora.",
            "Successfully defeat a walking corpse and follow it up by consuming plant-based nourishment.",
            "Battle and vanquish a zombie, afterwards partake in eating a plant.",
            "Combat with a revenant, bring it down and subsequently ingest a botanical item.",
            "Engage in a fight with a living dead creature, outfighting it, following which ingest green fodder."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE, Achievement.EAT_PLANT],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_COLLECT_IRON": {
        "instruction": "You need to collect some logs and mine some iron.",
        "instruction_paraphrases": [
            "You have to gather a few pieces of lumber and mine a bit of iron.",
            "Try amassing several chunks of timber along with a few bits of iron ore.",
            "You're required to accumulate a quantity of wood and obtain a decent amount of iron.",
            "The task involves getting hold of some wood from trees and unearthing certain amounts of iron deposits.",
            "Acquire a significant volume of tree-derived materials and excavate considerable traces of the metallic element iron."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.COLLECT_IRON],
            forbidden=[]
        )
    },

    "EAT_COW_COLLECT_IRON": {
        "instruction": "You need to consume beef from a bovine animal and gather some metal minerals.",
        "instruction_paraphrases": [
            "May you please eat some cow's meat and accumulate some iron ores.",
            "Could you kindly devour cow-flesh and assemble a collection of iron minerals?",
            "You have to feast upon bovine and accrue certain amounts of ferrum.",
            "I require you to ingest some beef and amass a few chunks of iron.",
            "The task involves feeding on flesh of a cow and mining to accumulate iron ores."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.EAT_COW, Achievement.COLLECT_IRON],
            forbidden=[]
        )
    },

    "GATHER_COAL_IRON_EAT_PLANT": {
        "instruction": "Gather coal, iron and eat a plant.",
        "instruction_paraphrases": [
            "Collect some coal and iron, and consume a plant.",
            "Mine for coal and iron, then eat some vegetables.",
            "Procure some coal and iron, following with plant consumption.",
            "Accrue deposits of coal and iron, then partake of some vegetation.",
            "Assemble an aggregation of coal and iron, before indulging in some herbivorous tendencies."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_COAL, Achievement.COLLECT_IRON, Achievement.EAT_PLANT],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_PLACE_FURNACE": {
        "instruction": "Create a stone pickaxe and install a furnace for use.",
        "instruction_paraphrases": [
            "Fabricate a pickaxe made of stone and put together a furnace.",
            "Make a stone pickaxe and have a furnace set up.",
            "Concoct a rock pickaxe and get a furnace installed.",
            "Craft a cobblestone pickaxe and establish a kiln.",
            "Construct a stone cutter and erect a furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.PLACE_FURNACE],
            forbidden=[]
        )
    },

    "EAT_PLANT_MAKE_STONE_PICKAXE_REPEAT": {
        "instruction": "Eat a plant, craft a stone pickaxe and then eat another plant.",
        "instruction_paraphrases": [
            "Devour a plant, construct a stone pickaxe and munch another plant.",
            "Consume some greenery, forge a stone digger, and nibble on another vegetable.",
            "Have a plant for a snack, fabricate a stone cutter, and feast on an additional flora.",
            "Ingest flora, assemble a rock digger, and partake in extra botany-based nourishment.",
            "Swallow greens, build a pebble chopping tool, and chow down another vegetative matter."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.EAT_PLANT, Achievement.MAKE_STONE_PICKAXE],
            forbidden=[]
        )
    },

    "PLACE_FURNACE_NO_MAKE_IRON_PICKAXE_ALLOW_SWORD": {
        "instruction": "Make sure you have placed the furnace and not built an iron pickaxe. You can make the iron sword though.",
        "instruction_paraphrases": [
            "Ensure the furnace is set but do not construct a pickaxe of iron. Feel free to create an iron sword.",
            "It's crucial to have established the furnace, but don't bother forming an iron pickaxe. You have permission to synthesize an iron sword.",
            "Having a furnace in place is necessary and avoid crafting an iron pickaxe, however, the creation of an iron sword is allowed.",
            "Confirm the furnace installation but refrain from constructing an iron pickaxe. Constructing an iron cutlass is allowable though.",
            "The furnace should be positioned appropriately, but the fabrication of an iron pickaxe should not be executed. However, forming an iron epee is permissible."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_FURNACE, Achievement.MAKE_IRON_SWORD],
            forbidden=[Achievement.MAKE_IRON_PICKAXE]
        )
    },

    "COLLECT_DRINK_NO_PLACE_TABLE": {
        "instruction": "Get a drink but don't place a workbench.",
        "instruction_paraphrases": [
            "Obtain a beverage, avoid setting up a table.",
            "Procure a liquid refreshment but restrain from furnishing a desk.",
            "Secure a thirst-quencher without positioning a work station.",
            "Acquire an aqueous solution and refrain from locating a worktable.",
            "Apprehend a drink though forbear from establishing a workstation."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DRINK],
            forbidden=[Achievement.PLACE_TABLE]
        )
    },

    "COLLECT_COAL_PLACE_PLANT_COLLECT_DRINK": {
        "instruction": "Collect some coal, place a plant and gather a drink.",
        "instruction_paraphrases": [
            "Retrieve some coal, position a plant and assemble a drink.",
            "Garner some bits of coal, establish a plant and fetch a beverage.",
            "Acquire a number of coals, situate a flora and collect a gulp.",
            "Obtain pieces of coal, set down a greenery and bring together a liquid nourishment.",
            "Accumulate deposits of coal, plant and secure a thirst-quenching liquid."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_COAL, Achievement.PLACE_PLANT, Achievement.COLLECT_DRINK],
            forbidden=[]
        )
    },

    "DEFEAT_ZOMBIE_PLACE_TABLE": {
        "instruction": "Defeat a zombie and then place a table.",
        "instruction_paraphrases": [
            "Kill a zombie and set up a desk.",
            "Eradicate the zombie and position a workbench.",
            "Eliminate one of the undead and establish a table.",
            "Overcome the walking dead and install a tabletop.",
            "Annihilate a monster from hell and put in place a work surface."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE, Achievement.PLACE_TABLE],
            forbidden=[]
        )
    },

    "COLLECT_STONE_PLACE_STONE_COLLECT_DRINK": {
        "instruction": "Collect stones, place them and get a drink.",
        "instruction_paraphrases": [
            "Gather rocks, set them down and grab a beverage.",
            "Acquire pebbles, position them accordingly and fetch a drink.",
            "Procure some cobblestones, arrange them suitably and have a refreshing drink.",
            "Amass a pile of stones, install them at an appropriate location and aid yourself to a drink.",
            "Assemble a collection of stone items, dispatch them in a certain configuration and partake in the enjoyment of a drink."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_STONE, Achievement.PLACE_STONE, Achievement.COLLECT_DRINK],
            forbidden=[]
        )
    },

    "PLACE_PLANT_PLACE_FURNACE": {
        "instruction": "Start by placing a plant, then continue with the placement of the furnace.",
        "instruction_paraphrases": [
            "First, position the plant, then proceed to set the furnace.",
            "The plant is the first to be situated, and following that, make sure the furnace is put into place.",
            "Begin with the positioning of the flora, after which the heating device should be arranged.",
            "Take a plant and put it down first. After doing that, you should continue with placing the furnace.",
            "To start, place a plant and following that you should lay the furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_PLANT, Achievement.PLACE_FURNACE],
            forbidden=[]
        )
    },

    "COLLECT_STONE_MAKE_STONE_SWORD": {
        "instruction": "First, collect some rocks. Then, make a stone sword.",
        "instruction_paraphrases": [
            "Start by gathering some stones; after that, forge a sword from the stones you've gathered.",
            "Your initial task is to amass a collection of rocks, then, employ these stones and manufacture a stone blade.",
            "The first course of action should involve you amassing an array of stones, then, employ these stones and fabricate a weapon of stone.",
            "The foremost task you must undertake requires you to procure an assortment of geological rocks, next fabricate a weapon of stone.",
            "Before anything else, you are to undertake the deposition of an accumulation of boulders, afterwards follow-through with the formation of a blade of stony constitution."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_STONE, Achievement.MAKE_STONE_SWORD],
            forbidden=[]
        )
    },

    "COLLECT_DIAMOND_MAKE_STONE_PICKAXE": {
        "instruction": "Gather some diamonds and make a stone pickaxe.",
        "instruction_paraphrases": [
            "Collect some diamonds and create a stone pickaxe.",
            "Acquire a few diamonds and craft a pickaxe made of stone.",
            "Procure a handful of diamonds and forge a stone pick.",
            "Amass a quantity of diamonds and fabricate a pick crafted from stones.",
            "Hoist in some diamond gems and construct a stone-based pickaxe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.MAKE_STONE_PICKAXE],
            forbidden=[]
        )
    },

    "MAKE_WOOD_PICKAXE_THEN_COLLECT_DIAMOND": {
        "instruction": "Craft a wooden pickaxe first, then start collecting some diamonds.",
        "instruction_paraphrases": [
            "Start by making a wooden pickaxe, then proceed to mining diamonds.",
            "Your first task is to create a wood miner's tool; once done, move on to gather diamond gems.",
            "Creating a lumber pick is a top priority; afterwards, you can gather a few precious diamonds.",
            "Engage in crafting a timber pickaxe prior to embarking on your diamond collection endeavour.",
            "Commence with the construction of a wood-based pickaxe and later move towards the accumulation of several diamond stones."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_PICKAXE, Achievement.COLLECT_DIAMOND],
            forbidden=[]
        )
    },

    "COLLECT_COAL_MAKE_IRON_PICKAXE_EAT_PLANT": {
        "instruction": "Please, gather some coal, create an iron pickaxe and eat a plant.",
        "instruction_paraphrases": [
            "Could you please mine some coal, forge an iron pickaxe and consume a plant?",
            "Collect a bit of coal, create a pickaxe made of iron and have a plant for food.",
            "Obtain some coal, manufacture an iron harvesting tool and eat greenery.",
            "Secure a quota of coal, assemble a miner's tool of iron and nourish yourself with a plant.",
            "Could you, kindly, procure a small batch of coal, put together a mineral extractor made of iron and ingest some vegetation?"
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_COAL, Achievement.MAKE_IRON_PICKAXE, Achievement.EAT_PLANT],
            forbidden=[]
        )
    },

    "WAKE_UP_PLACE_TABLE_NO_PLACE_PLANT": {
        "instruction": "You need to wake up, place your workbench and do not plant anything.",
        "instruction_paraphrases": [
            "Start by waking up, then set up your workbench, and remember not to plant anything.",
            "Before anything else, wake up, then place your workbench, yet avoid planting any seeds.",
            "Your tasks are to awaken, position your craft table, and abstain from any form of planting.",
            "The main actions you need to perform are rising from sleep, setting the crafting table in place, and steering clear of any kind of cultivation.",
            "You must rouse yourself from sleep, establish your workstation, and refrain from engaging in any horticultural activities."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.WAKE_UP, Achievement.PLACE_TABLE],
            forbidden=[Achievement.PLACE_PLANT]
        )
    },

    "COLLECT_COAL": {
        "instruction": "Collect some coal",
        "instruction_paraphrases": [
            "Kindly gather some coal",
            "Can you procure some coal?",
            "I need you to harvest some coal",
            "Could you accumulate some black minerals for me?",
            "Ensure to have some coal in your inventory"
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_COAL],
            forbidden=[]
        )
    },

    "WAKE_UP": {
        "instruction": "Please wake up.",
        "instruction_paraphrases": [
            "Could you please awaken?",
            "I need you to rise and shine.",
            "It's time for you to wake up.",
            "You must awaken now.",
            "Can you rouse yourself from sleep?"
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.WAKE_UP],
            forbidden=[]
        )
    }
}


# TODO: need to check how many synonyms are used

easy_test_other_params = {
    "EAT_COW_MAKE_STONE_SWORD": {
        "instruction": "Eat a cow and craft a stone sword.",
        "instruction_paraphrases": [
            "Consume beef and forge a stone blade.",
            "Eat cow meat and create a sword from stone.",
            "Savor beef and construct a stone sword.",
            "Devour a meal from a cow and make a stone sword.",
            "Enjoy beef and build a sword out of stone."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.EAT_COW, Achievement.MAKE_STONE_SWORD],
            forbidden=[]
        )
    },

    "PLACE_PLANT_DEFEAT_SKELETON": {
        "instruction": "Place a plant and defeat a skeleton.",
        "instruction_paraphrases": [
            "Set a plant into the soil and destroy a skeleton.",
            "Position a plant and eliminate a skeletal enemy.",
            "Plant a green sprout and defeat a skeleton.",
            "Drop a plant and vanquish a skeleton warrior.",
            "Install a plant and take down a bone-clad foe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_PLANT, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "DEFEAT_SKELETON_NO_DEFEAT_ZOMBIE": {
        "instruction": "Defeat a skeleton but do not kill a zombie.",
        "instruction_paraphrases": [
            "Take down a skeleton and leave zombies alone.",
            "Eliminate a skeleton while avoiding zombies.",
            "Destroy a skeletal enemy but do not engage with zombies.",
            "Fight a skeleton and spare the undead creatures.",
            "Vanquish a skeleton but refrain from fighting zombies."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_SKELETON],
            forbidden=[Achievement.DEFEAT_ZOMBIE]
        )
    },

    "MAKE_WOOD_SWORD_DEFEAT_SKELETON": {
        "instruction": "Craft a wooden sword and defeat a skeleton.",
        "instruction_paraphrases": [
            "Make a sword out of wood and destroy a skeleton.",
            "Craft a wooden blade and take down a skeletal enemy.",
            "Forge a wooden weapon and defeat a skeleton warrior.",
            "Build a sword from wood and vanquish a skeleton.",
            "Create a wooden sword and eliminate a skeletal foe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_SWORD, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_COLLECT_IRON": {
        "instruction": "Craft a stone pickaxe and collect iron.",
        "instruction_paraphrases": [
            "Forge a stone pickaxe and mine some iron.",
            "Create a mining tool from stone and gather iron ore.",
            "Build a durable pickaxe and extract iron from the ground.",
            "Make a stone pickaxe and collect metallic resources.",
            "Craft a stone pickaxe and retrieve iron from a vein."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.COLLECT_IRON],
            forbidden=[]
        )
    },

    "COLLECT_DIAMOND_MAKE_STONE_PICKAXE": {
        "instruction": "Collect a diamond and create a stone pickaxe.",
        "instruction_paraphrases": [
            "Find and gather a precious gem, then make a pickaxe out of stone.",
            "Initiate the collection of a diamond and proceed to fabricate a pickaxe using rock.",
            "Acquire a diamond first, and afterwards construct a stone miner's tool.",
            "Please find a sparkling gem, and then make a stone pickaxe.",
            "Secure a diamond, then manufacture a stone pickaxe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.MAKE_STONE_PICKAXE],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_MAKE_STONE_SWORD": {
        "instruction": "Gather some wood and create a Stone Sword.",
        "instruction_paraphrases": [
            "Collect timber and craft a blade of stone.",
            "Accumulate logs and manufacture a stone saber.",
            "Harvest wood and forge a sword from stone.",
            "Amass some lumber and make a weapon out of stone.",
            "Hoard some wooden materials and produce a stone weapon."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.MAKE_STONE_SWORD],
            forbidden=[]
        )
    },

    "PLACE_STONE_EAT_PLANT_DEFEAT_SKELETON": {
        "instruction": "Place a stone, eat a plant, and defeat a skeleton.",
        "instruction_paraphrases": [
            "Put down a rock, consume a herb, and conquer a skeleton.",
            "Set a stone in place, feed on a vegetable, and overcome a skeleton.",
            "Lay a stone, ingest a plant, and vanquish a skeleton.",
            "Position a rock, eat a plant, and triumph over a skeleton.",
            "Place a boulder, eat some greenery, and slay a skeleton."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_STONE, Achievement.EAT_PLANT, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "COLLECT_DRINK_NO_PLACE_FURNACE": {
        "instruction": "Please gather a drink but do not put down a furnace.",
        "instruction_paraphrases": [
            "Kindly collect liquid refreshments but avoid setting up any furnace.",
            "Pick up some beverages but refrain from placing a furnace.",
            "Collect a drink, but do not install a furnace anywhere.",
            "Obtain a beverage and make sure no furnace is placed.",
            "Gather drinks but avoid setting up a furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DRINK],
            forbidden=[Achievement.PLACE_FURNACE]
        )
    },

    "DEFEAT_ZOMBIE_MAKE_IRON_SWORD": {
        "instruction": "Defeat the zombie and make an iron sword.",
        "instruction_paraphrases": [
            "Vanquish the undead and forge a sword from iron.",
            "Overcome a zombie and fashion an iron blade.",
            "Conquer a living dead and shape a blade out of iron.",
            "Neutralize a zombie and create a weapon made from iron.",
            "Destroy a zombie and build an iron sword."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE, Achievement.MAKE_IRON_SWORD],
            forbidden=[]
        )
    },

    "PLACE_PLANT_DEFEAT_ZOMBIE": {
        "instruction": "Plant an object and defeat a zombie.",
        "instruction_paraphrases": [
            "Sow a plant and destroy a zombie.",
            "Cultivate a seedling and take down a walker.",
            "Establish a greenery and conquer an undead.",
            "Place a sapling and vanquish a zombie.",
            "Set down a plant and slay a zombie."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_PLANT, Achievement.DEFEAT_ZOMBIE],
            forbidden=[]
        )
    },

    "DEFEAT_SKELETON_COLLECT_WOOD_NO_PLACE_PLANT": {
        "instruction": "Beat the skeleton but don't plant anything and gather wood.",
        "instruction_paraphrases": [
            "Vanquish the skeleton, eschew planting and obtain timber.",
            "Defeat a skeleton, avoid planting, and collect wood.",
            "Kill the skeleton, skip planting, and gather logs.",
            "Take down the skeleton, abstain from planting, and harvest wood.",
            "Slay the skeleton, do not plant, and collect some wood."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_SKELETON, Achievement.COLLECT_WOOD],
            forbidden=[Achievement.PLACE_PLANT]
        )
    },

    "DEFEAT_ZOMBIE_PLACE_STONE_MAKE_WOOD_SWORD": {
        "instruction": "Defeat a zombie, place a stone and make a wooden sword.",
        "instruction_paraphrases": [
            "Bring down a zombie, set down a rock, and craft a wooden blade.",
            "Kill a zombie, lay a stone, and forge a wooden sword.",
            "Defeat the zombie, position a boulder, and build a wood sword.",
            "Vanquish a zombie, place a stone, and create a wooden weapon.",
            "Slay a zombie, drop a rock, and assemble a wooden sword."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE, Achievement.PLACE_STONE, Achievement.MAKE_WOOD_SWORD],
            forbidden=[]
        )
    },

    "COLLECT_DIAMOND_PLACE_PLANT_COLLECT_WOOD": {
        "instruction": "Collect diamonds, place a plant and gather wood.",
        "instruction_paraphrases": [
            "Acquire some precious gems, plant a sapling, and collect logs.",
            "Mine diamonds, plant a tree, and gather timber.",
            "Get diamonds, set down a plant, and collect wood.",
            "Obtain diamonds, plant a seedling, and harvest wood.",
            "Collect gem stones, place a plant, and gather lumber."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.PLACE_PLANT, Achievement.COLLECT_WOOD],
            forbidden=[]
        )
    },

    "MAKE_IRON_PICKAXE_NO_COLLECT_DRINK_MAKE_WOOD_SWORD": {
        "instruction": "Forge an iron pickaxe, avoid obtaining any drinks, and make a wooden sword.",
        "instruction_paraphrases": [
            "Craft an iron pickaxe, don't collect drinks, and build a wooden sword.",
            "Make an iron pickaxe, skip drink collection, and forge a wood sword.",
            "Create an iron miner's tool, avoid gathering beverages, and craft a wood blade.",
            "Forge a metal pick, no drinks, then craft a wooden sword.",
            "Produce an iron pickaxe, abstain from collecting drinks, and assemble a wood sword."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_IRON_PICKAXE, Achievement.MAKE_WOOD_SWORD],
            forbidden=[Achievement.COLLECT_DRINK]
        )
    },

    "NO_MAKE_WOOD_SWORD_PLACE_FURNACE": {
        "instruction": "Please make sure you do not craft a wooden sword. But, you should place a furnace.",
        "instruction_paraphrases": [
            "Avoid creating a wooden blade, but set up a furnace.",
            "Don't craft a wood sword; instead install a furnace.",
            "Refrain from making a wooden sword and put down a furnace.",
            "Skip fabricating a wood sword, and install a furnace.",
            "Hold off on a wooden weapon, but make sure the furnace is placed."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_FURNACE],
            forbidden=[Achievement.MAKE_WOOD_SWORD]
        )
    },

    "PLACE_STONE_WAKE_UP_COLLECT_IRON": {
        "instruction": "Put a stone, wake up and collect some iron.",
        "instruction_paraphrases": [
            "Place a rock, then wake up and gather iron.",
            "Set down a stone, rise from sleep, and collect iron.",
            "Lay a boulder, awaken, and mine some iron.",
            "Drop a stone, get up, and pick up iron.",
            "Position a stone, wake yourself, and collect iron."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_STONE, Achievement.WAKE_UP, Achievement.COLLECT_IRON],
            forbidden=[]
        )
    },

    "PLACE_PLANT_AND_WAKE_UP": {
        "instruction": "Place a plant and wake up.",
        "instruction_paraphrases": [
            "Put down a sapling and then rouse from sleep.",
            "Set a plant in place and awaken.",
            "Plant a seed and stir from slumber.",
            "Establish a sprout and then wake up.",
            "Place a seedling and rouse yourself."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_PLANT, Achievement.WAKE_UP],
            forbidden=[]
        )
    },

    "MAKE_WOOD_PICKAXE_WOOD_SWORD_DEFEAT_SKELETON": {
        "instruction": "Make a wooden pickaxe, slay a skeleton with a wooden sword, and defeat a skeleton.",
        "instruction_paraphrases": [
            "Craft a wood pickaxe, fight a skeleton with a wood sword, and vanquish it.",
            "Forge a wooden pickaxe, use a wooden sword against a skeleton, and kill it.",
            "Build a wood tool, then slay a skeleton with a wood blade, and defeat it again.",
            "Create a timber pickaxe, engage a skeleton using your wooden sword, and overcome it.",
            "Make a wood pickaxe, battle a skeleton with a wood sword, and emerge victorious."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_WOOD_PICKAXE, Achievement.MAKE_WOOD_SWORD, Achievement.DEFEAT_SKELETON],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_EAT_COW_EAT_PLANT": {
        "instruction": "Make a stone pickaxe, eat a cow and eat a plant.",
        "instruction_paraphrases": [
            "Forge a stone pickaxe, consume beef, and eat a plant.",
            "Build a rock pickaxe, devour cow meat, and munch on some greenery.",
            "Create a stone miner's tool, feast on beef, and eat a plant.",
            "Craft a stone cutter, eat cow steak, and then eat a plant.",
            "Construct a pickaxe from stone, eat a cow, and consume a plant."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.EAT_COW, Achievement.EAT_PLANT],
            forbidden=[]
        )
    },

    "COLLECT_DIAMOND_MAKE_STONE_SWORD": {
        "instruction": "Collect diamonds and craft a stone sword.",
        "instruction_paraphrases": [
            "Find some diamonds and make a stone blade.",
            "Mine diamonds and forge a sword from stone.",
            "Gather diamonds then craft a stone sword.",
            "Collect diamond gems, then build a stone weapon.",
            "Acquire diamonds and create a stone sword."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.MAKE_STONE_SWORD],
            forbidden=[]
        )
    },

    "PLACE_STONE_PLACE_TABLE_NO_PLACE_PLANT": {
        "instruction": "Set down the stone and the table, but do not place the plant.",
        "instruction_paraphrases": [
            "Put the rock and the workbench down, but refrain from placing a plant.",
            "Position the stone and the desk, but avoid planting a sapling.",
            "Place a boulder and a table, but do not plant anything.",
            "Lay down a rock and a work surface, but skip the plant.",
            "Install the stone and the tabletop, but do not set a plant."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_STONE, Achievement.PLACE_TABLE],
            forbidden=[Achievement.PLACE_PLANT]
        )
    },

    "PLACE_TABLE_NO_PLACE_PLANT": {
        "instruction": "Make sure to place a crafting table but avoid planting anything.",
        "instruction_paraphrases": [
            "Set up the crafting table but do not put down any plants.",
            "Install a workbench but refrain from planting saplings.",
            "Position the crafting station, but stay away from planting.",
            "Place the crafting bench but do not plant anything.",
            "Arrange the worktable and avoid sowing seeds."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_TABLE],
            forbidden=[Achievement.PLACE_PLANT]
        )
    },

    "COLLECT_WOOD_DEFEAT_SKELETON_COLLECT_SAPLING": {
        "instruction": "Please gather wood, defeat a skeleton and collect a sapling.",
        "instruction_paraphrases": [
            "Collect timber, slay a skeleton and pick up a sapling.",
            "Gather wood, defeat a skeleton and secure a seedling.",
            "Harvest logs, vanquish a skeleton and collect a young plant.",
            "Obtain wood, kill a skeleton and pick up a sapling.",
            "Amass lumber, defeat a skeleton and gather a sapling."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.DEFEAT_SKELETON, Achievement.COLLECT_SAPLING],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_NO_PLACE_PLANT": {
        "instruction": "Gather some timber but avoid planting anything.",
        "instruction_paraphrases": [
            "Collect wood but do not plant any saplings.",
            "Gather logs and refrain from placing plants.",
            "Amass lumber and skip planting.",
            "Harvest wood and avoid planting seeds.",
            "Obtain wood and do not plant."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD],
            forbidden=[Achievement.PLACE_PLANT]
        )
    },

    "COLLECT_DIAMOND_PLACE_FURNACE": {
        "instruction": "Collect some diamond and place a furnace.",
        "instruction_paraphrases": [
            "Find a diamond and set up a furnace.",
            "Gather a diamond then install a furnace.",
            "Acquire diamond and position a furnace.",
            "Obtain diamond and put down a furnace.",
            "Collect a diamond and place a furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.PLACE_FURNACE],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_EAT_COW_PLACE_FURNACE": {
        "instruction": "Craft a stone pickaxe, consume some beef and set up a furnace.",
        "instruction_paraphrases": [
            "Make a stone pickaxe, eat cow meat and place a furnace.",
            "Forge a stone pickaxe, feast on beef and install a furnace.",
            "Create a stone pickaxe, devour beef and erect a furnace.",
            "Build a stone pickaxe, eat a cow and set up a furnace.",
            "Construct a stone pickaxe, consume beef and place a furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.EAT_COW, Achievement.PLACE_FURNACE],
            forbidden=[]
        )
    },

    "PLACE_TABLE_COLLECT_SAPLING_COLLECT_DRINK": {
        "instruction": "Make sure you have placed a table, collected a sapling, and gathered a drink.",
        "instruction_paraphrases": [
            "Place a table, pick up a sapling, and get a drink.",
            "Set down the table, collect a seedling, and acquire a beverage.",
            "Install a bench, gather a sapling, and fetch a drink.",
            "Put up a worktable, collect a young plant, and grab a drink.",
            "Establish a table, pick a sapling, and secure a drink."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_TABLE, Achievement.COLLECT_SAPLING, Achievement.COLLECT_DRINK],
            forbidden=[]
        )
    },

    "COLLECT_WOOD_EAT_PLANT_NO_PLACE_PLANT": {
        "instruction": "You need to gather some lumber and consume a plant, just make sure you don't plant anything.",
        "instruction_paraphrases": [
            "Collect wood and eat a plant, but do not plant anything.",
            "Gather timber, eat vegetation, and skip planting.",
            "Harvest wood, consume a plant, and avoid planting.",
            "Amass logs, eat a plant, and do not plant.",
            "Obtain wood, eat greenery, and avoid sowing."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_WOOD, Achievement.EAT_PLANT],
            forbidden=[Achievement.PLACE_PLANT]
        )
    },

    "COLLECT_DRINK_COLLECT_SAPLING_PLACE_PLANT": {
        "instruction": "Collect a drink, gather a sapling and then place a plant.",
        "instruction_paraphrases": [
            "Get a drink, pick up a sapling, and plant it.",
            "Grab a beverage, collect a seedling, and plant it.",
            "Fetch a drink, secure a sapling, and place it.",
            "Acquire a beverage, gather a sapling, and plant it.",
            "Obtain a drink, collect a sapling, and set it down."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DRINK, Achievement.COLLECT_SAPLING, Achievement.PLACE_PLANT],
            forbidden=[]
        )
    },

    "PLACE_STONE_EAT_PLANT_COLLECT_COAL": {
        "instruction": "Place a stone, eat a plant, and collect some coal.",
        "instruction_paraphrases": [
            "Lay a stone, eat a plant, and mine coal.",
            "Set down a stone, eat greenery, and gather coal.",
            "Drop a rock, eat a plant, and collect coal.",
            "Position a stone, consume vegetation, and fetch coal.",
            "Place a boulder, eat a plant, and pick up coal."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_STONE, Achievement.EAT_PLANT, Achievement.COLLECT_COAL],
            forbidden=[]
        )
    },

    "NO_MAKE_WOOD_SWORD_COLLECT_SAPLING": {
        "instruction": "Don't craft a wooden sword but make sure to collect saplings.",
        "instruction_paraphrases": [
            "Avoid making a wooden sword but gather saplings.",
            "Do not forge a wood sword; instead collect saplings.",
            "Skip the wooden sword and pick up saplings.",
            "Hold off on a wooden sword, focus on collecting saplings.",
            "Refrain from crafting a wooden sword and gather saplings."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_SAPLING],
            forbidden=[Achievement.MAKE_WOOD_SWORD]
        )
    },

    "COLLECT_SAPLING_MAKE_WOOD_PICKAXE_MAKE_IRON_SWORD": {
        "instruction": "First, accumulate the sapling. Then, craft a wooden pickaxe. Finally, forge an iron sword.",
        "instruction_paraphrases": [
            "Gather a sapling, then make a wood pickaxe, and finally craft an iron sword.",
            "Collect a seedling, build a wooden pickaxe, and then forge an iron sword.",
            "Pick up a sapling, craft a wood pickaxe, and finish by making an iron sword.",
            "Secure a young plant, assemble a wood tool, and complete with an iron sword.",
            "Obtain a sapling, create a wooden pickaxe, and lastly forge an iron sword."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_SAPLING, Achievement.MAKE_WOOD_PICKAXE, Achievement.MAKE_IRON_SWORD],
            forbidden=[]
        )
    },

    "COLLECT_SAPLING_EAT_COW": {
        "instruction": "Collect a sapling and then eat a cow.",
        "instruction_paraphrases": [
            "Pick up a sapling, then consume a cow.",
            "Gather a young plant and eat cow meat.",
            "Collect a seedling and feast on a cow.",
            "Grab a sapling and afterwards eat beef.",
            "Acquire a sapling, then eat a cow."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_SAPLING, Achievement.EAT_COW],
            forbidden=[]
        )
    },

    "NO_MAKE_STONE_SWORD_COLLECT_DIAMOND_EAT_PLANT": {
        "instruction": "Avoid crafting a stone sword, locate and pick up a diamond, and make sure to consume a plant.",
        "instruction_paraphrases": [
            "Don't make a stone sword; instead collect a diamond and eat a plant.",
            "Skip crafting a stone blade, mine a diamond, and eat vegetation.",
            "Forego the stone sword, pick up a diamond, and consume a plant.",
            "Refrain from building a stone sword, gather a diamond, and eat a plant.",
            "Bypass the stone sword, secure a diamond, and eat a plant."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.EAT_PLANT],
            forbidden=[Achievement.MAKE_STONE_SWORD]
        )
    },

    "PLACE_FURNACE_MAKE_IRON_SWORD_NO_MAKE_WOOD_SWORD": {
        "instruction": "Make an iron sword, ensure you have not made a wooden sword and place a furnace.",
        "instruction_paraphrases": [
            "Forge an iron sword, skip the wooden sword and set up a furnace.",
            "Create an iron blade, do not make a wood sword, and install a furnace.",
            "Make an iron sword, avoid making a wooden sword, and place a furnace.",
            "Craft an iron sword, no wood sword, then put down a furnace.",
            "Build an iron sword, refrain from wood sword, and install a furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.PLACE_FURNACE, Achievement.MAKE_IRON_SWORD],
            forbidden=[Achievement.MAKE_WOOD_SWORD]
        )
    },

    "COLLECT_SAPLING_EAT_COW_MAKE_IRON_SWORD": {
        "instruction": "Collect a sapling, eat a cow, and make an iron sword.",
        "instruction_paraphrases": [
            "Gather a sapling, consume beef, and forge an iron sword.",
            "Pick up a sapling, eat a cow, and craft an iron blade.",
            "Collect a young plant, feast on cow meat, and build an iron sword.",
            "Obtain a sapling, eat beef, and then make an iron sword.",
            "Grab a sapling, devour cow, and forge an iron sword."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_SAPLING, Achievement.EAT_COW, Achievement.MAKE_IRON_SWORD],
            forbidden=[]
        )
    },

    "COLLECT_DIAMOND_DEFEAT_ZOMBIE": {
        "instruction": "Ensure that you have collected a diamond and defeated a zombie.",
        "instruction_paraphrases": [
            "Make sure you've picked up a diamond and beaten a zombie.",
            "Confirm you collected a diamond and defeated a zombie.",
            "Verify you mined a diamond and destroyed a zombie.",
            "Check that you have a diamond and have defeated a zombie.",
            "Ensure you have a diamond and that you defeated a zombie."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DIAMOND, Achievement.DEFEAT_ZOMBIE],
            forbidden=[]
        )
    },

    "DEFEAT_SKELETON_EAT_COW": {
        "instruction": "Ensure you have defeated the skeleton and consumed the cow.",
        "instruction_paraphrases": [
            "Make sure you've slain the skeleton and eaten the cow.",
            "Confirm you killed the skeleton and ate the cow.",
            "Verify you beat the skeleton and consumed a cow.",
            "Check that you defeated the skeleton and ate a cow.",
            "Ensure you vanquished the skeleton and consumed beef."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_SKELETON, Achievement.EAT_COW],
            forbidden=[]
        )
    },

    "DEFEAT_ZOMBIE_COLLECT_COAL_PLACE_STONE": {
        "instruction": "Defeat a zombie, get some coal and put down a stone.",
        "instruction_paraphrases": [
            "Kill a zombie, collect coal, then place a stone.",
            "Defeat the zombie, mine coal and lay a rock.",
            "Beat a zombie, gather coal, and drop a stone.",
            "Vanquish a zombie, get coal, and position a stone.",
            "Slay a zombie, collect some coal, and put down a rock."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_ZOMBIE, Achievement.COLLECT_COAL, Achievement.PLACE_STONE],
            forbidden=[]
        )
    },

    "MAKE_STONE_PICKAXE_MAKE_STONE_SWORD_NO_PLACE_FURNACE": {
        "instruction": "Construct a stone pickaxe and a stone sword, but do not set up a furnace.",
        "instruction_paraphrases": [
            "Make a stone pickaxe and sword but avoid placing a furnace.",
            "Craft both a stone pickaxe and sword, then skip the furnace.",
            "Forge a stone tool and blade, but do not install a furnace.",
            "Build a stone pickaxe and sword, while refraining from placing a furnace.",
            "Create stone mining and combat tools, and do not set up a furnace."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE, Achievement.MAKE_STONE_SWORD],
            forbidden=[Achievement.PLACE_FURNACE]
        )
    },

    "COLLECT_DRINK_DEFEAT_ZOMBIE": {
        "instruction": "Collect a drink and fight off a zombie.",
        "instruction_paraphrases": [
            "Get a beverage and then defeat a zombie.",
            "Fetch a drink and kill a zombie.",
            "Obtain a refreshment, then beat a zombie.",
            "Grab a drink and slay a zombie.",
            "Pick up a drink and vanquish a zombie."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.COLLECT_DRINK, Achievement.DEFEAT_ZOMBIE],
            forbidden=[]
        )
    },

    "NO_PLACE_FURNACE_MAKE_STONE_PICKAXE": {
        "instruction": "Ensure that you do not place the furnace but create a stone pickaxe.",
        "instruction_paraphrases": [
            "Don't install a furnace; instead make a stone pickaxe.",
            "Avoid placing a furnace and craft a stone pickaxe.",
            "Skip the furnace and build a stone pickaxe.",
            "Do not set up a furnace, but forge a stone pickaxe.",
            "Refrain from placing a furnace and produce a stone pickaxe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.MAKE_STONE_PICKAXE],
            forbidden=[Achievement.PLACE_FURNACE]
        )
    },

    "DEFEAT_SKELETON_PLACE_PLANT": {
        "instruction": "Defeat a skeleton and then place a plant.",
        "instruction_paraphrases": [
            "Slay a skeleton, then plant a sapling.",
            "Kill the skeleton and afterward place a plant.",
            "Defeat a skeleton and then set down a plant.",
            "Vanquish a skeleton, then put a plant.",
            "Overcome a skeleton and then plant a sapling."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
        "arguments": create_target_state(
            required=[Achievement.DEFEAT_SKELETON, Achievement.PLACE_PLANT],
            forbidden=[]
        )
    }
}


medium_test_parafrased = {}

medium_test_other_paramets = {}

hard_test_parafrased = {}

hard_test_other_paramets = {}