
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
"COLLECT_DRINK_AND_EAT_COW":{
    "instruction": "Collect a drink and eat a cow.",
    "instruction_paraphrases": [
      "Retrieve a beverage and consume beef.",
      "Find a drink and eat cow meat.",
      "Collect a liquid and savor cow flesh.",
      "Gather a drinkable item and devour beef.",
      "Acquire a drink and enjoy a meal from a cow."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_DRINK, Achievement.EAT_COW],
      forbidden=[]
    )
  },
"PLACE_STONE_AND_WAKE_UP":{
    "instruction": "Place a stone block and wake up.",
    "instruction_paraphrases": [
      "Set down a stone block and rise from sleep.",
      "Position a stone and awaken.",
      "Place a block of stone and stand up after resting.",
      "Install a stone block and shake off slumber.",
      "Drop a stone block and prepare for the day."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.PLACE_STONE, Achievement.WAKE_UP],
      forbidden=[]
    )
  },

"PLACE_FURNACE_AND_PLACE_STONE":{
    "instruction": "Place a furnace and a stone block.",
    "instruction_paraphrases": [
      "Set up a furnace and position a stone block.",
      "Install a smelter and place down a stone.",
      "Drop a furnace and a block of stone.",
      "Put a furnace and a stone in their spots.",
      "Arrange a furnace and a stone block nearby."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.PLACE_FURNACE, Achievement.PLACE_STONE],
      forbidden=[]
    )
  },
"EAT_COW_AND_MAKE_STONE_PICKAXE":{
    "instruction": "Eat a cow and craft a stone pickaxe.",
    "instruction_paraphrases": [
      "Consume beef and create a stone pickaxe.",
      "Eat cow meat and forge a stone mining tool.",
      "Savor a meal from a cow and craft a pickaxe from stone.",
      "Devour beef and assemble a stone pickaxe.",
      "Have a cow-based dish and make a stone pickaxe."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.EAT_COW, Achievement.MAKE_STONE_PICKAXE],
      forbidden=[]
    )
  },
"PLACE_PLANT_AND_DEFEAT_ZOMBIE":{
    "instruction": "Place a plant and defeat a zombie.",
    "instruction_paraphrases": [
      "Set a plant into the ground and eliminate a zombie.",
      "Position a plant and destroy an undead creature.",
      "Plant a shrub and take down a zombie.",
      "Drop a plant and vanquish a wandering zombie.",
      "Install a plant and defeat a night-stalking zombie."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.PLACE_PLANT, Achievement.DEFEAT_ZOMBIE],
      forbidden=[]
    )
  },
"PLACE_FURNACE_AND_MAKE_IRON_SWORD_NO_IRON_PICKAXE":{
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
"DEFEAT_ZOMBIE_NO_DEFEAT_SKELETON":{
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
"MAKE_STONE_SWORD_AND_DEFEAT_SKELETON":{
    "instruction": "Craft a stone sword and defeat a skeleton.",
    "instruction_paraphrases": [
      "Forge a stone blade and eliminate a skeletal enemy.",
      "Create a weapon from stone and take down a skeleton.",
      "Build a stone sword and vanquish a bone-clad foe.",
      "Make a sword out of stone and defeat a skeleton warrior.",
      "Construct a stone sword and destroy a skeleton."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_STONE_SWORD, Achievement.DEFEAT_SKELETON],
      forbidden=[]
    )
},
"MAKE_STONE_PICKAXE_AND_COLLECT_COAL":{
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
"MAKE_STONE_PICKAXE_NO_IRON_SWORD":{
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
"COLLECT_SAPLING_AND_COLLECT_IRON":{
    "instruction": "Collect a sapling and some iron in the game.",
    "instruction_paraphrases": [
      "Gather a young tree and iron ores.",
      "Pick up a plant shoot and mine some iron.",
      "Acquire a small tree and some iron minerals.",
      "Procure a budding plant and iron nuggets.",
      "Obtain a sprout and some iron deposit."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_SAPLING, Achievement.COLLECT_IRON],
      forbidden=[]
    )
},
"EAT_PLANT_NO_EAT_COW":{
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
"COLLECT_WOOD_PLACE_STONE_AND_MAKE_STONE_PICKAXE":{
    "instruction": "Collect some wood, place a rock and make a stone pickaxe.",
    "instruction_paraphrases": [
      "Gather some timber, put a boulder in place and craft a stone pickaxe.",
      "Pick up some lumber, set a pebble and construct a stone chopping tool.",
      "Amass some wooden materials, arrange a cobble, and produce a stony axe.",
      "Assemble some fragments of tree, designate a spot for a stone, and cobble together a pickaxe made of stone.",
      "Procure wood from the surroundings, ensure a rock is situated and forge a tool for excavation out of stone."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_WOOD, Achievement.PLACE_STONE, Achievement.MAKE_STONE_PICKAXE],
      forbidden=[]
    )
},
"PLACE_PLANT_NO_MAKE_STONE_SWORD":{
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
"COLLECT_DRINK_PLACE_PLANT_AND_DEFEAT_SKELETON":{
    "instruction": "Collect a drink, place a plant, and defeat a skeleton.",
    "instruction_paraphrases": [
      "Get your hands on a drink, grow a plant and defeat the skeleton.",
      "Procure a beverage, install a herb and overcome the skeleton.",
      "Find a drinkable item, put a flora, and conquer the skeleton.",
      "Secure a quenchable, situate a vegetal, and triumph over a skeleton.",
      "Acquire a potable, establish a botanical and vanquish the skeleton."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_DRINK, Achievement.PLACE_PLANT, Achievement.DEFEAT_SKELETON],
      forbidden=[]
    )
},
"WAKE_UP_DEFEAT_ZOMBIE_AND_COLLECT_DRINK":{
    "instruction": "You must wake up. Then, you need to defeat a zombie and lastly, fetch a drink for yourself.",
    "instruction_paraphrases": [
      "Get up from your sleep first. Post that, you must confront and win over a zombie. Lastly, make sure to obtain a drink.",
      "Rise from your rest first. Following this, it's important to tackle and overcome a zombie. In the end, secure a drink for your own self.",
      "You are required to awaken initially. Subsequent to this, it's crucial to resist and triumph over a zombie. To conclude, purchase a drink.",
      "You're needed to come out of your slumber at first. Upon accomplishing this, a zombie must be encountered and defeated. Ultimately, procure a beverage for yourself.",
      "You are supposed to wake up first. Then, a zombie needs to be challenged and defeated. Finally, get hold of a beverage."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.WAKE_UP, Achievement.DEFEAT_ZOMBIE, Achievement.COLLECT_DRINK],
      forbidden=[]
    )
},
"MAKE_STONE_SWORD_AND_COLLECT_SAPLING_NO_MAKE_IRON_SWORD":{
    "instruction": "Don't create an Iron Sword. You need to, however, craft a Stone Sword and gather a Sapling.",
    "instruction_paraphrases": [
      "Make sure you aren't crafting an Iron Sword. However, you need to both collect a Sapling and manufacture a Stone Sword.",
      "You must not create an Iron Sword. Still, gather a Sapling and fashion a Stone Sword.",
      "Without making an Iron Sword, you have to garner a Sapling and bring into existence a Stone Sword.",
      "Regardless of what you do, don't craft an Iron Sword. But be sure to make a Stone Sword and collect some saplings.",
      "Without producing an Iron Sword, you must collect a Sapling and build a Stone Sword with all haste."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_STONE_SWORD, Achievement.COLLECT_SAPLING],
      forbidden=[Achievement.MAKE_IRON_SWORD]
    )
},
"COLLECT_IRON_MAKE_WOOD_PICKAXE_AND_DEFEAT_SKELETON":{
    "instruction": "Gather some iron, make a wooden pickaxe and defeat a skeleton.",
    "instruction_paraphrases": [
      "Please defeat a skeleton, after crafting a wooden pickaxe and collecting some iron.",
      "Your tasks: Craft a pickaxe from wood, defeat a bone-rattler, and acquire some iron.",
      "Collect some iron ores, construct a pickaxe using wood, and also ensure you vanquish a skeleton.",
      "I need you to construct a wood-tipped pickaxe, defeat a skeleton warrior and gather some iron ores."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_IRON, Achievement.MAKE_WOOD_PICKAXE, Achievement.DEFEAT_SKELETON],
      forbidden=[]
    )
},
"COLLECT_STONE_DEFEAT_SKELETON_AND_COLLECT_COAL":{
    "instruction": "Collect some stone, defeat a skeleton and gather coal.",
    "instruction_paraphrases": [
      "Please procure some rock, vanquish a skeleton and amass coal.",
      "Can you amass stone, exterminate a skeleton and gather some coal?",
      "Your task is to gather rock, obliterate a skeleton and accumulate some coal.",
      "You ought to collect rock, defeat a bony undead creature and mine some coal.",
      "Your duty is to procure stone, overcome a skeleton and obtain coal."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_STONE, Achievement.DEFEAT_SKELETON, Achievement.COLLECT_COAL],
      forbidden=[]
    )
},
"MAKE_STONE_SWORD_AND_WAKE_UP":{
    "instruction": "Please, make a stone sword and then wake up.",
    "instruction_paraphrases": [
      "Create a stone sword and then you must wake up.",
      "I need you to wake up after you have constructed a stone blade.",
      "Can you craft a rock sword and then arise?",
      "Could you produce a weapon made of stone, and then awaken?",
      "Can you manufacture an armament composed of sedimentary material, subsequent to your awakening?"
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_STONE_SWORD, Achievement.WAKE_UP],
      forbidden=[]
    )
},
"MAKE_WOOD_SWORD_AND_PLACE_PLANT":{
    "instruction": "Craft a wooden sword and cultivate a plant.",
    "instruction_paraphrases": [
      "Make your own timber blade and place a sapling.",
      "Create a wooden weapon and improve the environment around you by growing a plant.",
      "Chisel a wooden falcata and utilize it in horticulture to grow a sapling.",
      "Craftsmanship with timber should result in a sword and some efforts of botany to place a young plant.",
      "Focus your woodworking skills to craft a wooden saber and engage in some green landscaping by cultivating a plant."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_WOOD_SWORD, Achievement.PLACE_PLANT],
      forbidden=[]
    )
},
"COLLECT_STONE_AND_MAKE_IRON_SWORD":{
    "instruction": "Please gather rock and then make an iron sword.",
    "instruction_paraphrases": [
      "Go on a mission to collect some stones and then transform some iron into a sword.",
      "Your task is to obtain some cobblestone, and after that, forge a blade utilizing iron.",
      "You need to secure boulders before proceeding to manufacture a tool of offense made of iron.",
      "I require you to accumulate rocky resources and then proceed to the creation of a sword made solemnly of iron.",
      "Could you please head out, gather some dense rock and then utilize the collected iron to create a strong offensive tool?"
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_STONE, Achievement.MAKE_IRON_SWORD],
      forbidden=[]
    )
},
"COLLECT_DIAMOND_COLLECT_IRON_AND_EAT_COW":{
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
"MAKE_WOOD_PICKAXE_AND_DEFEAT_SKELETON":{
    "instruction": "Make a wooden axe and defeat a skeleton, but in no specific order.",
    "instruction_paraphrases": [
      "Your target is to craft a wooden pickaxe and defeat a skeleton. You can complete these tasks in any sequence.",
      "Please, take on the skeleton after or before crafting a wooden pickaxe.",
      "Your missions are to construct a wooden axe and take down a skeleton. Order doesn't matter.",
      "You need to accomplish two tasks. First is to build a wood pickaxe and second is to conquer a skeleton. You are free to choose the order.",
      "Your objectives include two tasks, creating a wooden tool for chopping, specifically a pickaxe, in addition to overcoming a skeleton enemy. You're allowed to tackle them in any order you prefer."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_WOOD_PICKAXE, Achievement.DEFEAT_SKELETON],
      forbidden=[]
    )
},
"COLLECT_WOOD_AND_COLLECT_IRON":{
    "instruction": "You need to gather some wood and iron.",
    "instruction_paraphrases": [
      "It's essential for you to collect both timber and iron ore.",
      "Your task is harvesting wood and mining for some iron.",
      "You are required to amass both lumber and iron materials.",
      "Procure both wooden logs and iron elements as a part of the task.",
      "It's incumbent on you to accumulate components of both wood and iron."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_WOOD, Achievement.COLLECT_IRON],
      forbidden=[]
    )
},
"COLLECT_SAPLING_AND_COLLECT_COAL":{
    "instruction": "Find a tree sapling and collect a piece of coal.",
    "instruction_paraphrases": [
      "Search for a small tree, then obtain a piece of charcoal.",
      "Scour for a young tree, followed by securing a piece of black mineral known as coal.",
      "Hunt down a tree sprout and then gather a coal fragment.",
      "Begin by locating a tree seedling, conclude by retrieving a lump of coal.",
      "Initiate your quest by identifying a sapling, following it up by the collection of a piece of coal."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_SAPLING, Achievement.COLLECT_COAL],
      forbidden=[]
    )
},
"COLLECT_DRINK_NO_MAKE_STONE_SWORD":{
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
"MAKE_WOOD_PICKAXE_NO_PLACE_PLANT":{
    "instruction": "Craft a wooden pickaxe but avoid planting anything.",
    "instruction_paraphrases": [
      "Make sure to construct a wooden digging tool, but don't place any plants.",
      "Your task is to build a pickaxe out of wood, however, refrain from cultivating any plants.",
      "I want you to create a wooden mining instrument, but it's important that you don't engage in any plantations.",
      "It's essential that you manufacture a pickaxe utilizing wood, though make sure not to involve yourself in any gardening activities.",
      "The objective is to fabricate a timber-sourced pickaxe while deliberately abstaining from any form of plant deployment."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_WOOD_PICKAXE],
      forbidden=[Achievement.PLACE_PLANT]
    )
},
"PLACE_FURNACE_AND_MAKE_IRON_SWORD_NO_MAKE_IRON_PICKAXE":{
    "instruction": "Make sure you have placed the furnace and not built an iron pickaxe. You can make the iron sword though.",
    "instruction_paraphrases": [
      "Confirm that you have set up the furnace. You should not create an iron pickaxe, yet making an iron sword is allowed.",
      "Please ensure that you have sited the furnace but have not constructed an iron pickaxe. Nonetheless, forging an iron sword is permissible.",
      "It is imperative that you have installed the furnace and refrained from assembling an iron pickaxe, while on the other hand the creation of an iron sword is acceptable.",
      "The prerequisites are that the furnace has been positioned appropriately and the formation of an iron pickaxe has been avoided. However, you are permitted to produce an iron sword as it's necessary.",
      "You are required to verify the placement of the furnace and abstain from manufacturing an iron pickaxe. However, you have the authorization to craft an iron sword."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.PLACE_FURNACE, Achievement.MAKE_IRON_SWORD],
      forbidden=[Achievement.MAKE_IRON_PICKAXE]
    )
},
"COLLECT_COAL_PLACE_PLANT_AND_COLLECT_DRINK":{
    "instruction": "Collect some coal, place a plant and gather a drink.",
    "instruction_paraphrases": [
      "Gather coal, place foliage and obtain some beverages.",
      "Accumulate some coal, deposit a shrub and acquire liquid refreshment.",
      "Assemble a quantity of carbon, install flora and collect hydration.",
      "Amass lumps of coal, situate a herbaceous plant and garner a type of drinkable liquid.",
      "Cull a pile of burnable carbon substance, position a botanical entity and stock up on a form of potable."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_COAL, Achievement.PLACE_PLANT, Achievement.COLLECT_DRINK],
      forbidden=[]
    )
},
"PLACE_PLANT_AND_PLACE_FURNACE":{
    "instruction": "Place a plant first, then place the furnace.",
    "instruction_paraphrases": [
      "First put the plant, then put the furnace.",
      "Before you put the furnace, make sure you have placed the plant.",
      "Only after placing a plant should you place the furnace.",
      "In order of operations, place the plant before you place the furnace.",
      "After putting down the plant, your next task should be to put down the furnace."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.PLACE_PLANT, Achievement.PLACE_FURNACE],
      forbidden=[]
    )
},
"COLLECT_STONE_AND_MAKE_STONE_SWORD":{
    "instruction": "First, collect some rocks. Then, make a stone sword.",
    "instruction_paraphrases": [
      "Gather some stones and then craft a sword out of stone.",
      "To start off, you should amass some rocks. Following that, use the rocks to put together a sword made of stone.",
      "You should begin by acquiring a couple of stones. Subsequently, you should manufacture a sword by using the stones.",
      "At first, you need to get a hold of some stones. Once you've done that, the next step is to construct a stone sword.",
      "To begin, amass a stockpile of rocks. With those in hand, your next objective is to assemble a weapon of warfare, specifically a sword, composed entirely of stone."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_STONE, Achievement.MAKE_STONE_SWORD],
      forbidden=[]
    )
},
"COLLECT_DIAMOND_AND_MAKE_STONE_PICKAXE":{
    "instruction": "Gather some diamonds and produce a stone pickaxe.",
    "instruction_paraphrases": [
      "Acquire a few gems and make a stone mining tool.",
      "Procure some sparklers and construct a rock digging instrument.",
      "Obtain several diamonds and fabricate a stone pick.",
      "Secure a handful of precious stones and assemble a stone picker.",
      "Ensure to amass diamonds and put together a stone excavator."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_DIAMOND, Achievement.MAKE_STONE_PICKAXE],
      forbidden=[]
    )
},
"MAKE_WOOD_PICKAXE_AND_COLLECT_DIAMOND":{
    "instruction": "Create a wooden pickaxe and then gather some diamonds.",
    "instruction_paraphrases": [
      "Begin by crafting a wood pickaxe and proceed to collect diamonds.",
      "An essential task for you is to fabricate a timber chopping tool, and subsequently, you must discover precious stones.",
      "The first chore is to construct a lumber pick and follow it up with diamond acquisition.",
      "Primarily, the technical creation of a wooden pick is required. Pursue this with the excavation of diamonds.",
      "Post the manufacture of a pick out of wood, search and harvest the glistening diamonds."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.MAKE_WOOD_PICKAXE, Achievement.COLLECT_DIAMOND],
      forbidden=[]
    )
},
"COLLECT_COAL_MAKE_IRON_PICKAXE_AND_EAT_PLANT":{
    "instruction": "Please, gather some coal, create an iron pickaxe and eat a plant.",
    "instruction_paraphrases": [
      "Collect coal, craft an iron pick, and consume vegetable.",
      "Can you obtain some coal, forge a pickaxe made of iron and ingest a herb?",
      "I need you to secure some coal, manufacture a pickax using iron and devour a flora.",
      "Kindly accumulate charred remains, produce a mining tool of iron and munch on greens.",
      "Please assemble some cinder remnants, fabricate an excavation instrument out of iron, and ingest a leafy foodstuff."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.COLLECT_COAL, Achievement.MAKE_IRON_PICKAXE, Achievement.EAT_PLANT],
      forbidden=[]
    )
},
"WAKE_UP_AND_PLACE_TABLE_NO_PLACE_PLANT":{
    "instruction": "Wake up, place the workbench and avoid planting anything.",
    "instruction_paraphrases": [
      "Rise, set up the woodworking table, and refrain from putting down any flora.",
      "Get up, put the craft table in place and avoid any cultivation.",
      "Stand up, position your bench for crafting and make sure you don't do any planting.",
      "Get yourself up, position your carpentry table strategically and make sure not to engage in any cultivation activities.",
      "Arise, systematically set up your table for crafting and remember you aren't supposed to plant anything."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_ACHIEVEMENTS,
    "arguments": create_target_state(
      required=[Achievement.WAKE_UP, Achievement.PLACE_TABLE],
      forbidden=[Achievement.PLACE_PLANT]
    )
},
"COLLECT_IRON_NO_PLACE_PLANT":{
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