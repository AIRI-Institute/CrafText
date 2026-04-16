from craftext.environment.scenarious.checkers.target_state import TargetState, LocalizaPlacingState
from craftext.environment.craftext_constants import Scenarios, BlockType

def create_target_state(object_inventory_enum, object_to_place, count_to_collect, count_to_stand):
    target_achievements = LocalizaPlacingState(object_inventory_enum, object_to_place, count_to_collect, count_to_stand)
    return TargetState(Localization_placing=target_achievements)

easy_test_paraphrased = {
  "INSTRUCTION_PLACE_STONE_LEFT_OF_FURNACE_1_1": {
    "instruction": "Place a stone one block to the left of the furnace.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position a rock a unit to the west of the kiln.",
      "Should you find yourself in the vicinity of the furnace, it is your duty to move a stone one block to its left.",
      "In spite of its weight and hardness, your task is to adjust a unit to the left, a rock bearing the vicinity of the kiln.",
      "In the shadowy realm of the searing furnace, thy charge is to take a stone, sturdy and unyielding, and relocate it a block to the west, under the vigilant watch of the ever-hungry kiln.",
      "In the relentless dance of stone and fire, a single stone must find itself moved a measure to the left of the ever-watching furnace, a silent testament to the delicate balance of space and flame."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.FURNACE, 1, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.FURNACE, 1, 1)"
  },
  "INSTRUCTION_PLACE_PLANT_ABOVE_GRASS_2_3": {
    "instruction": "Place a plant three blocks above the grass.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position a shrub trio of squares over the turf.",
      "While positioning a shrub, ensure that it is precisely three spaces higher in altitude than the adjacent verdant grassland.",
      "While arranging vegetation, ensure to situate the leaves-bearing entity exactly a trio of units above the green carpet of nature.",
      "In the deepest vestige of your mind's eye, envision yourself situating a lush foliage of green, a verdant being of nature, thrice the measure upwards from the tender, unbroken carpet of emerald grounds.",
      "Imagine the quiet choreography of a dance between a plant and the natural world, where the plant makes a leap upwards, precisely three steps above the green, a kind of floating ballet above the simple, clear truth of the grass."
    ],
    "arguments": create_target_state(BlockType.PLANT, BlockType.GRASS, 2, 3),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.GRASS, 2, 3)"
  },
  "INSTRUCTION_PLACE_STONE_ABOVE_IRON_2_2": {
    "instruction": "Place a stone two blocks above the iron.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Set a rock two squares beyond the metal.",
      "Where the iron is located, put a stone two blocks higher.",
      "Set a rock, which is to be placed two squares higher, beyond the metal.",
      "Beyond the stature of iron, in the realm of the stone, rest it in its dwelling, twice as high as yonder iron.",
      "In the woven world of iron and stone, set a stone to float two steps closer to the sky than the iron."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.IRON, 2, 2),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.IRON, 2, 2)"
  },
  "INSTRUCTION_PLACE_STONE_LEFT_OF_COAL_1_4": {
    "instruction": "Place the stone 4 blocks to the left of the coal.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Set the rock four units left of the charcoal.",
      "Without faltering, it's critical to arrange the stone precisely four blocks to the side from the coal.",
      "Ensure that the boulder is correctly stationed a precise four units to the western point of the charcoal.",
      "In yonder realm, 'tis critical to bestow thine stone four steps to the arms of the left, distanced from the depthless night's coal.",
      "The stone, its weight tangible and familiar, must find itself a new resting place four blocks distance to the left of the coal, its black heart unseen but always present."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.COAL, 1, 4),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.COAL, 1, 4)"
  },
  "INSTRUCTION_PLACE_CRAFTING_TABLE_NORTH_OF_PLANT_2_3": {
    "instruction": "Please place the Crafting Table three blocks north from the Plant.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Kindly position the Workbench trio of cubes upwards from the Flora.",
      "Would you be so kind as to set the Crafting Table, aiming it three blocks to the north, our reference being the Plant?",
      "Could you, with sincerity, locate the Artisan Desk in a trio of cubic spaces towards the zenith, taking the Flora as our reference point?",
      "Upon thy request, prithee, arrange yon Crafting Board in a measure of three stones northwards, as counted from the humble Plant, a token of nature's flourish.",
      "In your hands a task rests: to extend the earth a mere three blocks northwards, and there, as if sprouting like vegetation itself, place our Crafting Table, creating a harmonious link between our work and the Plant."
    ],
    "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PLANT, 2, 3),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.PLANT, 2, 3)"
  },
  "INSTRUCTION_PLACE_STONE_ABOVE_COAL_2_1": {
    "instruction": "Place a stone one block above the coal.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position a rock 1 unit higher than the carbon.",
      "The operation consists of situating a single stone one stretch elevated from the coal.",
      "In order to execute the task, one would locate a boulder precisely one tier ascending from the carbonaceous compound.",
      "In the realm of ancient miners, your task would be to deposit a fragment of the earth firmament, a lone block above the heart of our energy source, the coveted coal.",
      "In the tapestry of this world measured in blocks, a stone must find its place, not alongside, but rather, one degree above the monochromatic heart that beats coal."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.COAL, 2, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.COAL, 2, 1)"
  },
  "INSTRUCTION_PLACE_STONE_ABOVE_TREE_2_4": {
    "instruction": "Place the stone 4 blocks above the tree.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the rock quartet cubes atop the timber.",
      "The stone shall be positioned in such a manner that it is four blocks higher than the tree.",
      "The mineral, replacing perfectly, must land snugly upon four cubes, superior to the tree's apex.",
      "In the timeless age of old, brought forth was a decree to station yonder rock, a quartet of steps in height, above the elder tree's crown.",
      "With thoughtfulness, let the stone find itself four steps towards the heavens, beyond the reach of the tree's outstretched emerald fingers."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.TREE, 2, 4),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.TREE, 2, 4)"
  },
  "INSTRUCTION_PLACE_STONE_RIGHT_OF_STONE_0_4": {
    "instruction": "Place a stone four blocks to the right of another stone.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the rock four squares towards the right of another rock.",
      "The desired location of the stone is, if we consider the initial piece of stone as a reference point, measured at an interval of four blocks to its right.",
      "Determine position for the pebble as four units to the starboard side of the initial fragment of rock.",
      "In the vast terrain, with the enduring stone as our waypoint, we are tasked to set forth another rock, steadfastly at a distance of four boulders to the right.",
      "In the grand tapestry of the world, we take a stone, not just any stone but a silent testament of time, and we navigate its journey four steps towards the sunrise from another of its kin."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.STONE, 0, 4),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.STONE, 0, 4)"
  },
  "INSTRUCTION_PLACE_STONE_BELOW_TREE_3_5": {
    "instruction": "Place the stone five blocks below the tree.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the rock five sections beneath the oak.",
      "It is the tree, under which five blocks down, the stone must be placed.",
      "The rock ought to be situated five segments lower than the tall tree.",
      "Down the length of the quiet path, let the hardy stone rest nobly, hidden five stones under the boughs of the ancient oak.",
      "Let the stone heed the call of the earth's deep belly, journeying five steps down under the comforting shadow of the tree."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.TREE, 3, 5),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.TREE, 3, 5)"
  },
  "INSTRUCTION_PLACE_STONE_LEFT_OF_STONE_1_2": {
    "instruction": "Place a stone, two units to the left of another stone.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Set a pebble, duo steps to the west of a different boulder.",
      "A stone is to be positioned, such that it lies two measures to the left of another stone.",
      "A pebble is to be situated, ensuring it falls a duo distances westward of a different boulder.",
      "Lay ye a stone, in two strides to the left of another, aged as olden times.",
      "In the grand tapestry of stone placements, one finds itself a humble two paths to the left of its kindred stone."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.STONE, 1, 2),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.STONE, 1, 2)"
  },
  "INSTRUCTION_PLACE_FURNACE_LEFT_OF_STONE_1_4": {
    "instruction": "Place a furnace 4 blocks to the left of the stone.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Situate a kiln four units west of the rock.",
      "While the stone remains in its place, move four blocks to the left and position the furnace there.",
      "Preserving the rock's position, move the kiln four units westwards in an orderly fashion.",
      "In the land stretching westward from the enduring stone, place thou the furnace four strides distant.",
      "In the vast expanse that is the world, four measures to the left of the profound, unwavering stone, the crucible finds its place."
    ],
    "arguments": create_target_state(BlockType.FURNACE, BlockType.STONE, 1, 4),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.STONE, 1, 4)"
  },
  "INSTRUCTION_PLACE_PLANT_ABOVE_WATER_2_1": {
    "instruction": "Place a plant one block above the water.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Situate a flora one unit higher than the liquid.",
      "When one considers placing a plant, it ought to be precisely one block above the water.",
      "Consider situating a flora exactly one unit higher than the aqua.",
      "Duty calls to set a small living green, just one hewn stone's height above the murmuring cerulean abyss.",
      "In the dance of caretaking, let the plant find its home on a block, gently suspended above the whispering waters."
    ],
    "arguments": create_target_state(BlockType.PLANT, BlockType.WATER, 2, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.WATER, 2, 1)"
  },
  "INSTRUCTION_PLACE_CRAFTING_TABLE_LEFT_OF_PATH_1_5": {
    "instruction": "Place crafting table 5 blocks to the left of the path.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Set the artisan station 5 cubes to the west of the trail.",
      "The crafting table should be positioned 5 blocks on the left side, relative to the trail's course.",
      "Station the trade block five squares westward, in relation to the direction of the footpath.",
      "Depositing the table of creation, five spans to the left, in accordance to the pathway underfoot, as if the compass command so.",
      "Imagine the crafting table settled comfortably in its new location, five solid steps to the left of the meandering path, in harmony with the surrounding."
    ],
    "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PATH, 1, 5),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.PATH, 1, 5)"
  },
  "INSTRUCTION_PLACE_CRAFTING_TABLE_LEFT_OF_COAL_1_1": {
    "instruction": "Place the crafting table one block to the left of the coal.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the artisan's board a unit to the west of the carbon.",
      "Put the workbench exactly a singular space to what we commonly refer to as 'left', when referring to the solid fossil fuel, coal.",
      "To plant the worktable, seek a unit in the western direction adjacent to the lignite.",
      "In the manner of a thoughtful master craftsman, with careful deliberation, shift thine crafting table, a touch to the west, in relation to the great lump of ancient, dark coal, a fragment of grand eruptions past.",
      "In the stream of world-making, where every space holds truths, let the crafting table settle, subtly shifted one pace to the left, standing in gentle opposition to the ancient, silent relic of the earth, the coal."
    ],
    "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.COAL, 1, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.COAL, 1, 1)"
  },
  "INSTRUCTION_PLACE_CRAFTING_TABLE_BELOW_WOOD_3_5": {
    "instruction": "Place a crafting table 5 blocks below the wood.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Install a workbench five units underneath the timber.",
      "It is required to set a crafting table down, precisely five blocks beneath the wood.",
      "Position a workbench, making sure it's exactly five units below the layer of timber.",
      "A crafting table thou must position, albeit five stone's throw netherwards from the overhead timber, 'tis your quest.",
      "Mother Earth invites you to plant a crafting table, five breaths beneath the anchoring heart of the timber."
    ],
    "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.WOOD, 3, 5),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.WOOD, 3, 5)"
  },
  "INSTRUCTION_PLACE_STONE_BELOW_CRAFTING_TABLE_3_2": {
    "instruction": "Place the stone two blocks below the crafting table.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the rock a couple of units beneath the construction desk.",
      "The instruction, clear in its simplicity, is to put the stone exactly two blocks underneath the craftsman's table.",
      "Arrange the pebble precisely a duo of segments under the builder's bench.",
      "In the deep silence of twilight under the shadows of a looming oak, be thou the one to lay the boulder a pair of measures under the artisan's stand.",
      "At the heart of a quiet moment, the stone takes a journey two lengths downward, settling beneath the sacred table of creation."
    ],
    "arguments": create_target_state(BlockType.STONE, BlockType.CRAFTING_TABLE, 3, 2),
    "str_check_lambda": "place_object_relevant_to(BlockType.STONE, BlockType.CRAFTING_TABLE, 3, 2)"
  },
  "INSTRUCTION_PLACE_PLANT_RIGHT_OF_COAL_0_1": {
    "instruction": "Place a plant one block to the right of the coal.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position a flora one unit to the east of the carbon.",
      "Although the coal is situated in a given location, one must ensure that the plant is arranged one block to its right.",
      "While the carbon remains fixed at a certain point, correctly situate the flora one unit to its eastern direction.",
      "In the land where all things are meticulously placed, abide to set a green living creature, a plant of sorts, one stone's throw to the right of the dark, energy-converting carbon.",
      "In a delicate dance of placement and alignment, let a plant find its home one exact space to the right of the coal — a silent agreement between the living and the inert."
    ],
    "arguments": create_target_state(BlockType.PLANT, BlockType.COAL, 0, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.COAL, 0, 1)"
  },
  "INSTRUCTION_PLACE_FURNACE_RIGHT_OF_DIAMOND_0_2": {
    "instruction": "Place the furnace two units right of the diamond.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the kiln two steps to the right of the gemstone.",
      "The diamond has the furnace, two spaces to its right.",
      "Put the smelter two paces further to the right, relative to the jewel.",
      "In the realm where the hard stone of brightness finds its home, behold, two measures hence to the right, resides the fire-holder.",
      "Within this universe, a furnace dreamily finds its place two instances rightward of the diamond, merging heat with allure."
    ],
    "arguments": create_target_state(BlockType.FURNACE, BlockType.DIAMOND, 0, 2),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.DIAMOND, 0, 2)"
  },
  "INSTRUCTION_PLACE_FURNACE_LEFT_OF_GRASS_1_1": {
    "instruction": "Place a furnace one block to the left of the grass.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position a heater a single square leftwards of the turf.",
      "To the left of the grass, precisely one block away, establish your furnace.",
      "Immediately beside the turf's leftward side, set your heater at a distance of a single square.",
      "Upon the verdant meadows, askew to the dawn's side by but one span, perform thine task of placing yonder smelter.",
      "Next to the gentle embrace of the grass, go to the direction of the sunrise retreat, where only a measure of a single block separates; there, settle the furnace."
    ],
    "arguments": create_target_state(BlockType.FURNACE, BlockType.GRASS, 1, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.GRASS, 1, 1)"
  },
  "INSTRUCTION_PLACE_CRAFTING_TABLE_ABOVE_WATER_2_1": {
    "instruction": "Place the crafting table four blocks to the top of the water source.",
    "scenario_checker": Scenarios.LOCALIZATION_PLACE,
    "instruction_paraphrases": [
      "Position the creation desk four cubes above the water origin.",
      "At a point four blocks elevated from the water source, that is where the crafting table ought to be located.",
      "At a locale, exceeding the water origin by four cubes, you ought to station the creation desk.",
      "Upon the water's source, ascend a measure of four stone blocks and there, as if ordained, set ye a table of crafting.",
      "In the midst of the water source and its essence, aspire four stone blocks higher, whereupon lies the destiny of the crafting table, that mystical altar of creation."
    ],
    "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.WATER, 2, 1),
    "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.WATER, 2, 1)"
  }
}


easy_test_other_params = {
    "INSTRUCTION_PLACE_FURNACE_GRASS_0_5": {
        "instruction": "Place the furnace five squares to the right of the grass.",
        "instruction_paraphrases": [
            "Situate the furnace with a distance of five blocks to the right of grass.",
            "To the right of the grass, position the furnace five blocks away.",
            "First, locate the grass. Then, move five units to the right and place your furnace there.",
            "Identify the grass first. Afterward, position the furnace five squares towards the right.",
            "Find the grass, then navigate five squares rightward and situate the furnace."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.GRASS, 0, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_GRASS_3_1": {
        "instruction": "Place the crafting table one block below the grass block.",
        "instruction_paraphrases": [
            "Locate a grass block, and position the crafting table one block beneath it.",
            "Find a patch of grass and install a crafting table one space down.",
            "One block under a grass block, place your crafting table.",
            "Identify a grass block, and proceed to place the crafting table one block below it.",
            "Situate a crafting table at a distance of one block below a selected grass block."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.GRASS, 3, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_CRAFTING_TABLE_0_1": {
        "instruction": "Place furnace one block to the right of crafting table.",
        "instruction_paraphrases": [
            "Put the stove a block to the right of your workbench.",
            "To the right of the crafting station, move one block over and place the furnace there.",
            "Your crafting table is there, place the furnace one block to the right of it.",
            "Near your crafting table, on the right side specifically one block away, you should place your furnace.",
            "Your task is to position your furnace precisely one block to the right of the worktable, also known as the crafting table."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.CRAFTING_TABLE, 0, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_CRAFTING_TABLE_3_2": {
        "instruction": "Place the crafting table 2 blocks beneath the crafting table.",
        "instruction_paraphrases": [
            "Set up a crafting table two blocks below another crafting table.",
            "Could you put a workbench two blocks down from the existing one?",
            "Put the craft station just two blocks under the already present crafting table.",
            "Could you arrange a crafting table two blocks below the original crafting table?",
            "Move the workbench down by two blocks from the current one."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.CRAFTING_TABLE, 3, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_PLANT_IRON_0_3": {
        "instruction": "Place a plant 3 blocks to the right of the iron.",
        "instruction_paraphrases": [
            "Put a flower next to the iron, specifically 3 blocks to the right.",
            "Position the flora three squares rightward from the metallic mineral.",
            "To the right of the iron, with a gap of 3 blocks, place a plant.",
            "From the iron ore on the right side, 3 blocks away, establish a plant.",
            "Three blocks eastward from the iron is where you should locate the vegetation."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.PLANT, BlockType.IRON, 0, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_STONE_2_4": {
        "instruction": "Place the crafting table four blocks above the stone.",
        "instruction_paraphrases": [
            "Position the crafting table four spaces top of the rock.",
            "Arrange the workbench four blocks upward from the stone.",
            "Set the work station four spots to the north of the boulder.",
            "Situate the crafting table four notches above the stony block.",
            "Install the artisan table at a distance of four blocks to the top from the solid pebble."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.STONE, 2, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_FURNACE_3_5": {
        "instruction": "Place a stone 5 blocks below the furnace.",
        "instruction_paraphrases": [
            "Put a stone five blocks under the furnace.",
            "Set down a stone 5 squares beneath the firebox.",
            "Position a stone five spaces under the heating device.",
            "Situate a rock five blocks beneath the smelting unit.",
            "Locate a pebble five blocks under the molten ore oven."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.FURNACE, 3, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_PLANT_FURNACE_3_2": {
        "instruction": "Place a plant two blocks below the furnace.",
        "instruction_paraphrases": [
            "Put a plant two spaces under the heating unit.",
            "Set a plant a short distance below the heating appliance.",
            "Plant something two levels beneath the furnace.",
            "Position a plant two blocks directly under the smelter.",
            "Make sure there is a plant standing two blocks to the south of the heating system."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.PLANT, BlockType.FURNACE, 3, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_PLANT_3_1": {
        "instruction": "Place the crafting table 1 block below the plant.",
        "instruction_paraphrases": [
            "Can you put the create bench below the seeding for just one block?",
            "Set up the crafting desk at a distance of one unit underneath a botanical organism.",
            "Would you kindly position the crafting station down a block under the flora?",
            "You are expected to establish the craft workbench one space at a lower point relative to the botanical entity.",
            "The instructions request you to install a workstation for crafting precisely a single structural unit beneath a botanical growth."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PLANT, 3, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_PLANT_COAL_2_5": {
        "instruction": "Place the plant 5 blocks above the coal.",
        "instruction_paraphrases": [
            "You need to put the plant five blocks to the north of the lump of coal.",
            "Situate the seedling exactly five blocks on top of the piece of black rock.",
            "Locate the coal and arrange the plant five grids above it.",
            "Establish a position for the plant five spots upward from the anthracite.",
            "Find the bituminous and put the plant five steps above it."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.PLANT, BlockType.COAL, 2, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_STONE_3_4": {
        "instruction": "[EASY] PLACE CRAFTING_TABLE 4 BLOCKS TO THE BOTTOM OF STONE.",
        "instruction_paraphrases": [
            "Easily put a crafting table down four spaces below the rock.",
            "Quickly place the workbench 4 squares beneath the boulder.",
            "With simplicity, situate your crafting table four blocks southwards of the stone.",
            "Straightforwardly locate your assembly stand down four units from the pebble.",
            "Effortlessly position your crafting station exactly four segments down from the solid stone."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.STONE, 3, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_PLANT_1_2": {
        "instruction": "Place the crafting table two blocks left of the plant.",
        "instruction_paraphrases": [
            "Put the workbench to the left of the plant, precisely two blocks away.",
            "Find a plant and position the crafting table two squares to its left.",
            "Ensure the crafting table is located two blocks left of a plant.",
            "Position the workbench exactly two blocks left from the plant.",
            "Identify a plant and place the crafting table two units to its left."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PLANT, 1, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_STONE_1_4": {
        "instruction": "Place the crafting table 4 blocks away to the left of the stone.",
        "instruction_paraphrases": [
            "Can you position the crafting bench four squares on the left from the piece of rock?",
            "Your task is to find a spot left to the boulder to situate the work table there, four blocks away.",
            "Could you manage to set a workbench precisely four places on the left side of a cobblestone?",
            "In relation to a stone, put the crafting workstation at a distance of four spaces in a left direction.",
            "Identify a location that is exactly left of a stone, and then install a craft table four blocks apart from it."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.STONE, 1, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_DIAMOND_2_3": {
        "instruction": "Place the furnace 3 blocks above the diamond.",
        "instruction_paraphrases": [
            "Can you put the furnace three blocks to the top of the diamond?",
            "Situate the smelting equipment just three blocks above the precious gem.",
            "Could you install the oven three blocks North of the diamond rock?",
            "Position the heater three spots upward from the diamond.",
            "Establish the furnace exactly three units to the superior direction of the diamond."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.DIAMOND, 2, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_WATER_0_2": {
        "instruction": "Place the furnace 2 blocks to the right of water.",
        "instruction_paraphrases": [
            "Position the furnace two blocks right from the water.",
            "Put the furnace on the right side of the water, spaced by two blocks.",
            "Keep a two-block space from the water and place the furnace to its right side.",
            "Locate the area two blocks to the right of the water and place your furnace there.",
            "To the right of the water, leaving a distance of two blocks, position your furnace."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.WATER, 0, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_PLANT_3_4": {
        "instruction": "Place a crafting table 4 blocks below the plant.",
        "instruction_paraphrases": [
            "Position the workbench four squares beneath the greenery.",
            "Situate the crafting station four units under the flora.",
            "The plant should have a crafting table four blocks underneath it.",
            "Ensure the crafting desk is established four spots down from the vegetation.",
            "Below the botanical, you should find a crafting table set four blocks distant."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PLANT, 3, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_TREE_3_3": {
        "instruction": "Place a crafting table 3 blocks underneath the tree.",
        "instruction_paraphrases": [
            "Position a workbench three blocks directly below the timber.",
            "Put a craft station three units southward from the wood.",
            "Set up a table for crafting three blocks down from the arboreal.",
            "Erect a crafting counter three segments downward from the trunk.",
            "Position the crafting station three layers beneath the oak."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.TREE, 3, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_PLANT_2_1": {
        "instruction": "Place the furnace just above the plant.",
        "instruction_paraphrases": [
            "Situate the furnace directly up from the plant.",
            "Position the furnace one block north of the plant.",
            "Put the furnace right on top of the plant.",
            "The plant should have the furnace located one block above it.",
            "The furnace should be positioned one block up from the plant."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.PLANT, 2, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_STONE_3_2": {
        "instruction": "Place the crafting table two blocks below the stone.",
        "instruction_paraphrases": [
            "Set up the workbench a couple of blocks underneath the rock.",
            "Position the craft table precisely two squares beneath the stone.",
            "Install the crafting table exactly two steps down from the boulder.",
            "Locate the work stand accurately two blocks in the downward direction of the stone.",
            "Arrange your crafting desk two divisions under the geological rock."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.STONE, 3, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_PATH_3_3": {
        "instruction": "Place a crafting table 3 blocks below the path.",
        "instruction_paraphrases": [
            "Put the workbench three blocks underneath the path.",
            "Establish a crafting table three squares down from the path.",
            "Position the workstation three blocks to the bottom side of the path.",
            "Install a crafting surface 3 blocks under the defined path.",
            "Set a boardwalk down three blocks from the path."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PATH, 3, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_TREE_1_3": {
        "instruction": "Place the stone three blocks to the left of the tree.",
        "instruction_paraphrases": [
            "Put the stone three blocks leftwards of the tree.",
            "The tree should have the stone situated three blocks to its left.",
            "Next to the tree, position the stone three blocks leftward.",
            "Plant the stone on the left side of the tree, keeping a distance of three blocks.",
            "Leave a gap of three blocks to the left side of the tree, and then place the stone there."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.TREE, 1, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_GRASS_3_3": {
        "instruction": "Place the crafting table three blocks below the grass.",
        "instruction_paraphrases": [
            "Position the workbench at a three block distance downwards from the grass.",
            "Could you put the craftsman's table three blocks beneath the grass?",
            "Set the manufacturing table three sections south of the grass.",
            "Ensure the artisan's table is triple units downward of the grass.",
            "The crafting table needs to be three blocks under the grass, can you do that?"
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.GRASS, 3, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_WOOD_2_1": {
        "instruction": "Place the crafting table one block above the wood.",
        "instruction_paraphrases": [
            "Put the workbench a single block above the timber.",
            "Position the crafting station one layer on top of the wood.",
            "Establish the crafting desk one block on the upper side of the wood.",
            "Situate the assembly table exactly one block adjacent to the top of the wood.",
            "Set the construction bench at a distance of a single block from the wood, towards the top."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.WOOD, 2, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_PLANT_COAL_2_2": {
        "instruction": "Place the plant 2 blocks to the top of the coal.",
        "instruction_paraphrases": [
            "Position the plant two squares upward from the coal.",
            "Move the seedling 2 spaces above the chunk of coal.",
            "Set the plant precisely two blocks north of the coal piece.",
            "Arrange the sapling two units on top of the piece of coal.",
            "Two blocks above the lump of coal, that's where you should locate the plant."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.PLANT, BlockType.COAL, 2, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_PLANT_3_5": {
        "instruction": "Place the Furnace 5 blocks below the Plant.",
        "instruction_paraphrases": [
            "Can you put the Stove five units beneath the Seedling?",
            "You need to position the Heater five blocks under the Sprout.",
            "Please set the Forge five spaces underneath the Saplings.",
            "Ensure that the Kiln is situated five blocks at the downward side of the Shrub.",
            "I require the Hearth to be located five measures in a down direction from the Greenery."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.PLANT, 3, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_PATH_3_2": {
        "instruction": "Place the crafting table 2 blocks below the pathway.",
        "instruction_paraphrases": [
            "Can you put the workbench two blocks under the path?",
            "Please set the crafting table 2 units beneath the trail.",
            "I need you to install the crafting desk two steps below the walkway.",
            "Position the crafting stand a couple of blocks right underneath the route.",
            "Could you locate the construction table two bricks lower to that foot path?"
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PATH, 3, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_DIAMOND_0_5": {
        "instruction": "Place a crafting table 5 blocks to the right of the diamond block.",
        "instruction_paraphrases": [
            "Can you position a crafting station 5 blocks right from the diamond ore?",
            "Could you arrange a workbench 5 spaces to the east of the diamond chunk?",
            "Is it feasible to set a crafting table five squares on the starboard side of the diamond mass?",
            "Would you organize an assembly table a handful of steps due right from the gemstone block you count as diamond?",
            "Kindly locate an artisan's table a couple of strides rightwards from the diamond's resting place?"
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.DIAMOND, 0, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_WATER_3_3": {
        "instruction": "Place the stone three blocks below the water.",
        "instruction_paraphrases": [
            "Make sure to put the stone at a distance of three blocks down from the water.",
            "Kindly locate the stone three blocks beneath the water.",
            "Can you arrange the stone three blocks under the water?",
            "Could you place the stone three grids lower than water?",
            "Would you mind positioning the stone three blocks underneath the water?"
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.WATER, 3, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_IRON_2_1": {
        "instruction": "Place the Furnace one block to the top of the Iron.",
        "instruction_paraphrases": [
            "Position the Furnace exactly one block above the Iron.",
            "Set the Furnace at a spot that is one block higher than the Iron.",
            "Put the Furnace such that it is positioned one block to the top of the Iron.",
            "Can you locate the Furnace one block upward of the Iron?",
            "Ensure you place the Furnace one block on top of the Iron."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.IRON, 2, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_WATER_1_2": {
        "instruction": "Place the crafting table 2 blocks to the left of the water.",
        "instruction_paraphrases": [
            "Stick the crafting table two notches to the left of the water block.",
            "Put the crafting bench two blocks left from the water.",
            "You need to put down a crafting table, two squares to the left of the water.",
            "Two spots to the left side of the water, position the crafting station there.",
            "Proper positioning is crucial. Establish a crafting table two spaces westward from the water."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.WATER, 1, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_PLANT_PLANT_2_5": {
        "instruction": "Place a plant 5 blocks above another plant.",
        "instruction_paraphrases": [
            "Position a plant 5 spaces to the top of another plant.",
            "Locate a plant five blocks upwards from another flora.",
            "In relation to another greenery, put a plant five spots on its upper side.",
            "Relative to another vegetation, situate another plant five spots on its top.",
            "Organize a plant five units upwardly from another plant."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.PLANT, BlockType.PLANT, 2, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_WATER_2_4": {
        "instruction": "Place a stone block 4 squares above the water.",
        "instruction_paraphrases": [
            "Go up 4 spaces from the water and place a stone block.",
            "Position a stone 4 blocks north of the body of water.",
            "Above the water source, exactly 4 blocks higher, put a stone.",
            "In relation to the water, position a stone block four spaces upwards.",
            "Put the stone 4 squares towards the top from the water."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.WATER, 2, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_FURNACE_PATH_0_4": {
        "instruction": "Place furnace 4 blocks to the right of the path.",
        "instruction_paraphrases": [
            "Situate the stove four units on the path's right side.",
            "On the right side of the path, deploy the heater four blocks away.",
            "Establish the kiln at a distance of four blocks to the right of the pathway.",
            "To the path's immediate right, position the forge a mere four blocks away.",
            "Four blocks to the right of the trail, appropriately locate the fireplace."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.FURNACE, BlockType.PATH, 0, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_PATH_0_4": {
        "instruction": "Place a stone four blocks to the right of the path.",
        "instruction_paraphrases": [
            "Put a rock four squares to the right of the walkway.",
            "To the right side of the pathway, move four blocks then place the stone there.",
            "Find the path then move four spaces to the right; in that location, place a stone.",
            "From the path, make four steps towards the right and then position your stone.",
            "Locate the path. From there, navigate four blocks on the right side and set down a rock."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.PATH, 0, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_COAL_3_5": {
        "instruction": "Place a crafting table 5 blocks below the coal block.",
        "instruction_paraphrases": [
            "Kindly put a workbench five blocks beneath the coal rock.",
            "The duty for you is to set a crafting table down, precisely 5 blocks under the block of coal.",
            "Your task is to position a workshop table exactly five blocks lower than the coal unit.",
            "You are obligated to settle a station for crafting right five blocks underneath the piece of coal.",
            "I command you to establish an artificer's bench, specifically 5 cubes in the downward direction from the coal clump."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.COAL, 3, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_CRAFTING_TABLE_PLANT_3_3": {
        "instruction": "Place the crafting table three blocks below the plant.",
        "instruction_paraphrases": [
            "Position the crafting table 3 blocks beneath the plant.",
            "Put the workbench three blocks under the vegetation.",
            "Establish the crafting station three spaces south of the weed.",
            "Situate the bench for crafting trio of blocks downward from the shrub.",
            "Please setup the crafting mechanism three notches below from the flora."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.PLANT, 3, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_PLANT_IRON_1_1": {
        "instruction": "Place the plant one block left of the iron deposit.",
        "instruction_paraphrases": [
            "Can you put the plant to the left, exactly one block away from the iron source?",
            "Find an iron deposit and put a plant a block away on its left.",
            "Identify a block of iron and to its left place a plant, ensuring a distance of a single block.",
            "You need to place the plant one block apart on the left side of the iron deposit.",
            "Locate an iron deposit and to its immediate left with a gap of one block, please put a plant."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.PLANT, BlockType.IRON, 1, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_WATER_2_3": {
        "instruction": "Place a stone three blocks above the water.",
        "instruction_paraphrases": [
            "Position a rock three spaces north of the lake.",
            "Locate a stone three steps at the top of the water.",
            "Three blocks to the top of the water, locate a stone.",
            "Set a stone above the water, precisely three blocks away.",
            "Put a stone uphill from the water, with a distance of three blocks."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.WATER, 2, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_PATH_1_5": {
        "instruction": "Place a stone 5 blocks to the left of the path.",
        "instruction_paraphrases": [
            "Position a rock 5 blocks on the left side of the trail.",
            "Put a stone five blocks left of the pathway.",
            "Please set a rock on the pathway's left side, five blocks away.",
            "Could you deposit a stone five units towards the west of the path?",
            "Arrange a stone at a location that is 5 steps towards the left from the pathway."
        ],
        "scenario_checker": Scenarios.LOCALIZATION_PLACE,
        "arguments": create_target_state(BlockType.STONE, BlockType.PATH, 1, 5),
    },
        "INSTRUCTION_PLACE_PLANT_TREE_3_4": {
        "Instruction": "PLACE PLANT 4 BLOCKS TO THE BOTTOM OF TREE",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the vegetation four tiles beneath the tree",
            "Upon moving beneath the tree by four units, one must set the plant in place.",
            "Upon shifting beneath the arboreal entity by quartet units, the flora must be stationed.",
            "Upon sojourning four stones downward from the towering bark-clad sentinel, one must bestow the humble, green lifeform unto its destined place.",
            "Across four measures of space below the quiet whispering of the broad-leafed watcher, one feels the instinct to anchor the living green breath into the solidity of soil."
        ],
        "arguments": create_target_state(BlockType.PLANT, BlockType.TREE, 3, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.TREE, 3, 4)"
    }
,
    "INSTRUCTION_PLACE_STONE_GRASS_0_2": {
        "Instruction": "Place a stone block 2 squares to the right of the grass block.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Set a rock cube 2 units to the right of the verdant block.",
            "Establish the stone block in a position that requires two steps to the right from the grass block.",
            "Arrange a boulder square two measures eastward of the green square.",
            "Laying a cube crafted from the very bones of Earth, two paces to the orient of the verdant, grassy block.",
            "As if it were a dance, a piece of the stony earth is moved two steps right, where it comes to rest, echoing the harmony of the world, beside the block of vibrant green grass."
        ],
        "arguments": create_target_state(BlockType.STONE, BlockType.GRASS, 0, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.GRASS, 0, 2)"
    }
,
    "INSTRUCTION_PLACE_CRAFTING_TABLE_COAL_1_4": {
        "Instruction": "Place the crafting table four blocks to the left of the coal",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Set the artisan's bench four units to the port of the carbon",
            "Situate your crafting bench specifically four blocks away to the left from where the coal is placed",
            "Locate your artisan table precisely four units to the port side of the carbon storage area",
            "In the land betwixt the fifth block yonder from the blackened coal, set thine crafting table, sturdy and ready",
            "In the fabric of space, four steps to the left woven from the heart of coal, lay down the grounding of creation: the crafting table."
        ],
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.COAL, 1, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.COAL, 1, 4)"
    }
,
    "INSTRUCTION_PLACE_PLANT_GRASS_3_1": {
        "Instruction": "Position a Plant exactly one block below a patch of Grass.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Place a flora precisely a square beneath a clump of turf",
            "While there is a patch of grass, it is crucial that a plant is placed specifically one block beneath it",
            "Given a clump of turf, it becomes integral that a flora is posited precisely one square underneath",
            "In the land beneath the verdant emerald of grass, precisely a step of stone down, place thou the children of green with care",
            "In the underdeep, under a cool and silent spread of grass, a plant must find its home, nestled silently a block's distance away."
        ],
        "arguments": create_target_state(BlockType.PLANT, BlockType.GRASS, 3, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.GRASS, 3, 1)"
    }
,
    "INSTRUCTION_PLACE_PLANT_FURNACE_0_5": {
        "Instruction": "Place the Plant 5 blocks to the right of the Furnace",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the flora 5 units to the east of the kiln",
            "Wherever you find the furnace, make sure to locate the plant five blocks to its right",
            "Imagine where the kiln stands, then envision setting the flora precisely five units eastward of that point",
            "Just as one would wander five measured steps to the side of a dwarf's furnace, even so should one settle the sylvan life",
            "When the world arranges itself so that the kiln stands as a star, extend the world five steps further and let there be a spot for the verdant guest."
        ],
        "arguments": create_target_state(BlockType.PLANT, BlockType.FURNACE, 0, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.FURNACE, 0, 5)"
    }
,
    "INSTRUCTION_PLACE_CRAFTING_TABLE_WATER_0_5": {
        "Instruction": "Place the crafting table 5 blocks to the right of the water.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the fabrication platform 5 units to the starboard of the liquid.",
            "While maintaining a distance of 5 blocks away from the water, there you should position the crafting table on the right.",
            "Keeping a distance from the aqua equivalent to 5 blocks, it is necessary to place the workstation on the right-hand side.",
            "Situate the artisan's square, five strides to the eastern side of the aqua-vita, in the manner of an expert crafter under the sapphire dome of the sky.",
            "In the space that is five blocks right of the water, the crafting table finds its place, like a dancer finding her mark on a stage of blocks and water."
        ],
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.WATER, 0, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.WATER, 0, 5)"
    }
,
    "INSTRUCTION_PLACE_CRAFTING_TABLE_WATER_1_4": {
        "Instruction": "Place the crafting table 4 blocks to the left side of the water",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the creation platform 4 units to the westward of the liquid",
            "While considering the expanse of the area, move the crafting table 4 steps towards the left from the body of water",
            "Taking into account the spatial configuration, the creation platform must be stationed 4 units to the left of the aqueous expanse",
            "In the manner of craftsmen of old in the hallowed halls of stone beneath mountain-root, four measured-lengths westward of the water's gentle brook should thou move thine crafting table",
            "In the nuanced shadow dance of light and water, imagine the crafting table as a satellite, shifting subtly four spaces to the left from the water's lapping edge"
        ],
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.WATER, 1, 4),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.WATER, 1, 4)"
    }
,
    "INSTRUCTION_PLACE_FURNACE_FURNACE_1_2": {
        "Instruction": "Place the furnace 2 blocks to the left of the existing furnace.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the heater 2 units west of the current stove",
            "With a space of two blocks to the left, the furnace must settle just parallel to the old one",
            "Giving a gap of two units, the heater should be situated west of the present stove, making a sibling pair",
            "In days of yore, 'twas spoken thus: let the searing forge rest two spans to the autumn side of its brethren, the ancient fire-chamber",
            "With a resolute spirit, position the new heart of fire two paces westward; allowing it to echo a quiet kinship with the already ensconced furnace."
        ],
        "arguments": create_target_state(BlockType.FURNACE, BlockType.FURNACE, 1, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.FURNACE, 1, 2)"
    }
,
    "INSTRUCTION_PLACE_PLANT_STONE_3_5": {
        "Instruction": "Place the plant five blocks beneath the stone.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the flora five units under the rock.",
            "Despite being solid and unyielding, the stone had become a marker, signalling where the plant should be located: five blocks below it.",
            "Despite consisting of the hardened substance, the rock served as a beacon, indicating where the flora should be situated: a distance of five units beneath it.",
            "In a time long past, beneath the stalwart and relentless stone, a space was commanded for the green life, precisely five measures in the depth, in the heart of the earth itself.",
            "In the shadow of the immutable stone, five blocks down its guise, a place was whispered for the plant, a gentle murmur hinting of green life amidst the grey."
        ],
        "arguments": create_target_state(BlockType.PLANT, BlockType.STONE, 3, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.PLANT, BlockType.STONE, 3, 5)"
    }
,
    "INSTRUCTION_PLACE_STONE_TREE_0_2": {
        "Instruction": "Place a stone 2 blocks to the right of a tree.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Put a rock two squares to the right of a tree.",
            "Move a stone precisely to a location that is two blocks to the right of a tree.",
            "Implement the action of positioning a rock accurately to a spot that is two squares to the right of a tree.",
            "Wit thy hand place a stony piece, counted as two paces, to the eastward side of a lone tree.",
            "In the world of blocks and stones, set a stone into existence, two spaces to the right of the rooted being of a tree."
        ],
        "arguments": create_target_state(BlockType.STONE, BlockType.TREE, 0, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.TREE, 0, 2)"
    }
,
    "INSTRUCTION_PLACE_FURNACE_FURNACE_2_1": {
        "Instruction": "Place the furnace 1 block top of another furnace.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the kiln 1 unit above another kiln.",
            "The action to be taken involves setting a furnace precisely one block above an existing furnace.",
            "The action to be executed necessitates positioning a kiln exactly one unit on top of an existing kiln.",
            "In the ancient depths of any realm, a furnace ought to be stationed precisely one block above its fellow furnace, a site bespoke of the wisdom in structure.",
            "In the ceaseless dance of making and remaking, a furnace is to find its place in the world exactly a block's height above another furnace, as if whispering the secrets of fire to its kin."
        ],
        "arguments": create_target_state(BlockType.FURNACE, BlockType.FURNACE, 2, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.FURNACE, 2, 1)"
    }
,
    "INSTRUCTION_PLACE_CRAFTING_TABLE_STONE_1_5": {
        "Instruction": "Place the crafting table five blocks to the left of the stone.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Situate the assembly platform five cubes to the west of the rock.",
            "Allocate the crafting table at a distance of five blocks on the left side from the stone.",
            "Set the fabrication surface, five units to the west, adjacent to the hefty stone.",
            "Beseech you, position thy artisan's desk a handful of paces to the westward of yonder monumental stone, as firm as the foundation of the Earth.",
            "With careful deliberation, position the artisan's surface five lengths to the left, where it will find companionship with the stone ancient and immovable."
        ],
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.STONE, 1, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.STONE, 1, 5)"
    }
,
    "INSTRUCTION_PLACE_CRAFTING_TABLE_TREE_2_1": {
        "Instruction": "Place the crafting table one block to the top of the tree.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Situate the artisan's bench a notch above the arboreal being.",
            "Position the crafting table by moving it upward, at a distance of one block from the tree.",
            "Set up the artisan's surface by shifting it an iota higher, just distanced by a unity from the arboreal entity.",
            "In the tallest boughs of the tree, above where the eye naturally wanders, rests a craftsman's table, perched precariously one step removed from nature's towering sentinel.",
            "In the dance of objects and nature's rhythm, arise a new location for the crafting table, placed in a harmonious balance, a single step elevating it from the arms of the ancient tree."
        ],
        "arguments": create_target_state(BlockType.CRAFTING_TABLE, BlockType.TREE, 2, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.CRAFTING_TABLE, BlockType.TREE, 2, 1)"
    }
,
    "INSTRUCTION_PLACE_FURNACE_TREE_0_1": {
        "Instruction": "Place the furnace one block to the right of the tree.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the heater a unit to the east of the wood.",
            "The tree, standing alone, should have the furnace situated one block to its right.",
            "While the wood stands in isolation, orient the heater a single unit to its east.",
            "Let it be so that the foundry finds its home a solitary stride eastward of the lone tree, standing in the quiet solitude.",
            "In the meticulous design of our world, set the furnace just one step rightwards of the tree, the tree standing, unaccompanied and stoic in its place."
        ],
        "arguments": create_target_state(BlockType.FURNACE, BlockType.TREE, 0, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.TREE, 0, 1)"
    }
,
    "INSTRUCTION_PLACE_FURNACE_DIAMOND_2_5": {
        "Instruction": "Place the furnace five blocks to the top of the diamond",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Situate the oven five squares above the precious gem",
            "We must posit the furnace at a length of five blocks in a superior position to the diamond",
            "Attempting to relocate the oven, one shall find suitable the distance of five squares in a position superior to the valuable jewel",
            "In fair response to the call of the intrepid adventurer, one ought to station yonder furnace, guided by five paces towards the azure heavens, in grand ascendance above the gleaming diamond, hard-born of Earth's fiery heart.",
            "In the dance of creation, the furnace will find its place above the diamond, guided there by the deliberate discretion of five blocks, symbols of a measured intention and reflection of an unseen pattern."
        ],
        "arguments": create_target_state(BlockType.FURNACE, BlockType.DIAMOND, 2, 5),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.DIAMOND, 2, 5)"
    }
,
    "INSTRUCTION_PLACE_STONE_PATH_0_1": {
        "Instruction": "Please place the stone 1 block to the right of the pathway.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Kindly put the rock 1 unit to the starboard of the walkway.",
            "If you would be so kind, relocating the stone 1 block to the right of the pathway would be greatly appreciated.",
            "It would be of great assistance if you could relocate the rock, just one unit to the starboard of our course.",
            "May you find in your heart the will to shift yonder stone, a mere stride to the right of the ancient pathway traversed by many.",
            "Consider moving this particular stone - just a single step to the right of the pathway, a silent participant in countless journeys."
        ],
        "arguments": create_target_state(BlockType.STONE, BlockType.PATH, 0, 1),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.PATH, 0, 1)"
    }
,
    "INSTRUCTION_PLACE_FURNACE_PATH_2_3": {
        "Instruction": "Place furnace 3 blocks to the top of the path.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Situate the kiln 3 units above the trail.",
            "Consider the scenario where you are to position the furnace precisely 3 blocks skyward of the pathway.",
            "Envision a situation where you are called upon to position the kiln exactly 3 units north of the trek.",
            "In the vein of an epic saga, bestow thine hearthstone a score and thrice steps heavenwards from the trodden course.",
            "In the subtle whisperings of light and shadow, let the furnace find its place three measures away from the pathway, towards the sky."
        ],
        "arguments": create_target_state(BlockType.FURNACE, BlockType.PATH, 2, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.PATH, 2, 3)"
    }
,
    "INSTRUCTION_PLACE_STONE_PLANT_0_2": {
        "Instruction": "Place the stone 2 blocks to the right of the plant.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Position the rock two units to the east of the flora",
            "After passing the plant, proceed two blocks further and there you would locate the stone",
            "After meandering beyond the verdant growth, move two spaces further and there you'll find the rock",
            "In the vicinity where the green being breathes, two paces to the right's direction you must tread to find the stone of earth",
            "Where the plant whispers to the earth, two steps into the rightward breath of the world lays the stone"
        ],
        "arguments": create_target_state(BlockType.STONE, BlockType.PLANT, 0, 2),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.STONE, BlockType.PLANT, 0, 2)"
    }
,
    "INSTRUCTION_PLACE_FURNACE_PLANT_0_3": {
        "Instruction": "Place the furnace three blocks to the right of the plant.",
        "scenario_checker": 3,
        "Instruction_paraphrases": [
            "Set the heater three units to the east of the factory.",
            "In relation to the factory, the heater needs to be positioned exactly three blocks to the right.",
            "Positioning the heating unit precisely three divisions toward the east of the manufacturing plant is called for.",
            "In the manner of the ancients, thou shouldst position the forge three stones' walk to the true east of the greenery.",
            "In the heart of the industrial landscape, a heater, solitary and warm, to the world three steps eastward from its leafy neighbor, the factory, it should find its resting place."
        ],
        "arguments": create_target_state(BlockType.FURNACE, BlockType.PLANT, 0, 3),
        "str_check_lambda": "place_object_relevant_to(game_data, BlockType.FURNACE, BlockType.PLANT, 0, 3)"
    }
}



medium_test_parafrased = {}

### TODO: check the complexity
medium_test_other_paramets = {}
