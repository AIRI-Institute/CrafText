from craftext.environment.scenarious.checkers.target_state import TargetState, ConditionalPlacingState
from craftext.environment.craftext_constants import InventoryItems, BlockType, Scenarios


def create_target_state(object_inventory_enum, object_to_place, count_to_collect, count_to_stand):
    target_achievements = ConditionalPlacingState(object_inventory_enum, object_to_place, count_to_collect, count_to_stand)
    return TargetState(conditional_placing=target_achievements)

medium_test_parafrased = {
    "INSTRUCTION_PLACE_IRON_FURNACE_4_3": {
        "instruction": "Collect 4 iron and place 3 furnace.",
        "instruction_paraphrases": [
            "Acquire four pieces of iron and position three heating apparatus.",
            "While you must ensure the collection of four units of iron, it's also imperative to position three furnaces properly.",
            "It is your duty to procure four units of the dense, lustrous substance known as iron, and at the same time, accurately layout three heating devices.",
            "Gather ye forth iron in quantities fourfold, then rest three cauldrons made of stone in proper stead.",
            "As part of your journey, you are to seek out and gather four fragments of the earth's hidden iron, followed by the mindful placement of three vessels of warmth and creation."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.IRON, BlockType.FURNACE, 4, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_DIAMOND_STONE_3_1": {
        "instruction": "Collect three diamonds and place one rock on the map.",
        "instruction_paraphrases": [
            "Gather trio of gems and position a stone on the chart.",
            "Should you manage to assemble a trio of diamonds, a rock must then be situated upon the map.",
            "Should you successfully accumulate three gems, a stone must accordingly be situated on the chart.",
            "By the glimmer of Eärendil, assemble thou trio of sparkling hard-ices and with reverence position an ancient stone upon the cartographic parchment.",
            "In the stillness of time, you come into possession of three hard-icing gems, their glitter igniting the quiet. A sense of rightness evolves as you silently place a stone, hard-won from earth's bedrock, on the charted out expanse of the universe."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.STONE, 3, 1),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_WOOD_CRAFTING_TABLE_3_1": {
        "instruction": "Collect 3 pieces of wood and then place 1 crafting table.",
        "instruction_paraphrases": [
            "Gather three chunks of timber and subsequently position a solitary crafting table.",
            "While having gathered three slices of timber, you are to proceed by situating one crafting bench in your preferred location.",
            "In your possessions, possess three splinters of the forest's charm and, following this gathering, herald the manifestation of a humble artisan's perch.",
            "In a time of old, you would seek in the denseness of the untamed woodlands for three fragments of the timber of life, before setting down a crafter's shrine, a table of creation forged by the craft of ancient hands.",
            "In the bounty of the forest, find three pieces of the once living tree, and breathe existence into a crafting hearth to guide your way forth."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.WOOD, BlockType.CRAFTING_TABLE, 3, 1),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_CRAFTING_TABLE_2_5": {
        "instruction": "Collect 2 stones and place 5 crafting tables.",
        "instruction_paraphrases": [
            "Garner 2 pebbles and position 5 fabrication platforms.",
            "Collect two rocks, and once done, proceed to lay out five crafting tables.",
            "Garner a pair of pebbles, and once complete, position five tables for crafting.",
            "In the quiet recesses of the earth, gather two stones of aid and arrange, in solemn ceremony, five tables of crafting.",
            "As if drawn from the heart of the earth itself, pull forth two stones and settle, with intention, five platforms of creation."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.STONE, BlockType.CRAFTING_TABLE, 2, 5),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_COAL_FURNACE_4_3": {
        "instruction": "Pick up 4 pieces of coal and place down 3 furnaces.",
        "instruction_paraphrases": [
            "Collect four fragments of carbon and set down three ovens.",
            "Without delay, grab onto four chunks of carbon, only then to put in position three heating units.",
            "Acquire four stints of black stone, meanwhile, establish a trio of heating apparatus.",
            "Grasp thou four shards of the midnight mineral and situate hence three forges.",
            "In a world of rough and raw, gather four remnants of carbon and cradle down the three hearths."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.COAL, BlockType.FURNACE, 4, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_IRON_STONE_4_3": {
        "instruction": "Gather four pieces of iron and place three stones in your environment.",
        "instruction_paraphrases": [
            "Amass four iron segments and position three rocks in your surroundings.",
            "Having assembled four segments of iron, you should then arrange three stones within your immediate environment.",
            "Having accrued four fragments of metallic iron, one should arrange three boulders within the boundaries of one's surroundings.",
            "Four fragments of iron, ancient and sturdy, gather thee hither, and set in your surroundings the trio of stones, strong and enduring as the earth beneath us.",
            "Taking in your hands the strength of four pieces of iron, lay gently in your surroundings, the earth-bound trio of stones, as if they were an inherent part of your world."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.IRON, BlockType.STONE, 4, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_STONE_1_4": {
        "instruction": "Collect one piece of stone and then place four of them.",
        "instruction_paraphrases": [
            "Gather a single piece of rock and afterward position four of such.",
            "One piece of stone is to be collected prior to arranging four into place.",
            "Garner a sole fragment of boulder and subsequently locate four of these.",
            "In the spirit of the ancient masters, seize thyself one shard of the eternal mountain, and then, in deliberate design, bestow four of them upon their destined stations.",
            "Intuit an individual segment of stone and let it guide you, before establishing a quartet of them in their own harmony of placement."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.STONE, BlockType.STONE, 1, 4),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_FURNACE_1_4": {
        "instruction": "Collect one rock and place four furnaces.",
        "instruction_paraphrases": [
            "Gather a stone and establish four kilns.",
            "One should secure a singular stone while simultaneously setting up four separate furnaces.",
            "Procure a solitary pebble and proceed to position four individual kilns.",
            "With one hand, claim a stone solitary in days uncounted, and with your might, establish in the realm four everlasting furnaces.",
            "In a single quiet act, take hold of one earth's child, a stone, and breathe life into four servants of fire, the furnaces."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.STONE, BlockType.FURNACE, 1, 4),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_WOOD_PLANT_5_1": {
        "instruction": "Collect 5 pieces of wood and place 1 plant.",
        "instruction_paraphrases": [
            "Gather five logs and position a single flora.",
            "Assemble quintet fragments of timber and then, set one vegetation in their midst.",
            "Procure five elements of lumber and, thereafter, install an individual greenery.",
            "With care and deliberation, gather thou five parts of what once was the towering green, and in honour, situate a solitary sprout.",
            "Creep through the whispering woods, hands trembling as they grasp five pieces of wood only to softly lay down a single, trembling, plant."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.WOOD, BlockType.PLANT, 5, 1),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_COAL_FURNACE_2_1": {
        "instruction": "Collect 2 pieces of coal and place 1 furnace.",
        "instruction_paraphrases": [
            "Gather two chunks of coal and position one hearth.",
            "After you have accumulated two portions of coal, the next step is to set up a single furnace.",
            "After procuring a pair of coal fragments, proceed by situating a lone kiln.",
            "In thy journeys, seek to acquire twin fragments of the midnight stone, then, in solemn ritual, establish a solitary forge.",
            "In a deliberate act, unite two parts of coal with the world, then invite a solitary furnace into that space."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.COAL, BlockType.FURNACE, 2, 1),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_DIAMOND_STONE_5_1": {
        "instruction": "Collect 5 diamonds and place 1 stone.",
        "instruction_paraphrases": [
            "Accumulate 5 gemstones and position 1 rock.",
            "Once you have obtained 5 diamonds, your next task will be to set down a single stone.",
            "Acquire, in your possession, 5 precious diamonds, then followed by arranging 1 earthly stone.",
            "In your journey, seek you must, a hoard of 5 gleaming shards of the eternal earth's heart and once gained, bestow you shall, a single pebble unto its rightful place.",
            "In your hands, five shards of the starry cosmos gather and in turn, a stone, one and simple, is to be set into the silent cradle of the earth."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.STONE, 5, 1),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_COAL_PLANT_4_4": {
        "instruction": "Collect 4 pieces of coal and place 4 plants down.",
        "instruction_paraphrases": [
            "Collect 4 fragments of carbon and establish 4 flora.",
            "While amassing four constituents of anthracite, proceed with arranging four specimens of botany.",
            "While gathering four shards of black diamond, make preparations to position four instances of greenery.",
            "In thy ventures, seek ye the remnants of the earth's heart: four parts, coal-black and heavy with weight unseen. Then, in a procedure exhibiting equal parts care and reverence, lay down four children of nature, the emerald-born beacons of life.",
            "Gather not just four pieces of coal, but a quartet of solid silence, and then let four plants fall into their positions, like sun-kissed thoughts assuming form."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.COAL, BlockType.PLANT, 4, 4),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_COAL_STONE_2_3": {
        "instruction": "Collect 2 units of coal and place 3 stone blocks on the field.",
        "instruction_paraphrases": [
            "Acquire a pair of coal units and position 3 stone cubes in the terrain.",
            "After gathering two coal units, the next step is to position three blocks of stone in the field.",
            "Upon obtaining a duo of coal entities, the subsequent action is to precisely arrange three cubes of stone within the confines of the ground.",
            "Seek out and secure two pieces of the blackest coal and dutifully arrange upon the field, thrice hewn blocks of the hardest stone.",
            "In the quiet rhythm of reality, two pieces of primitive coal are acquired, their dark hearts echoing ancient fires. Then, in careful balance, three stone blocks find their place on the surface of the world’s field."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.COAL, BlockType.STONE, 2, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_WOOD_PLANT_4_5": {
        "instruction": "Gather 4 timber pieces and place 5 plants.",
        "instruction_paraphrases": [
            "Collect 4 wooden units and position 5 vegetation.",
            "The task requires you to first gather four pieces of timber, then to proceed by placing five plants.",
            "Acquire four units of wood and subsequently position five pieces of foliage within an orderly manner.",
            "There in yonder woodland, four fragments of the ancient barks are to be claimed and, in their stead, five leaf-bearers must find rest and life.",
            "In a rhythmic dance, gather four artifacts of the forest's skin, and in their silent echoing, place five children of Earth, green and thriving."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.WOOD, BlockType.PLANT, 4, 5),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_IRON_CRAFTING_TABLE_5_5": {
        "instruction": "Collect 5 iron and place 5 crafting tables.",
        "instruction_paraphrases": [
            "Gather five pieces of iron and position five crafting stations.",
            "For every crafting table put in place, an equivalent amount of iron, totaling five, should be amassed.",
            "For each crafting station positioned, a corresponding quantity of five iron should be collected.",
            "In the manner of a blacksmith of yore, congregating quintet of iron ores, lay down quintet of tables of crafted wonders.",
            "There is a rhythm to the gathering of five items of iron, a cadence mirrored in the placement of five tables that are, themselves, dedicated to crafting."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.IRON, BlockType.CRAFTING_TABLE, 5, 5),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_IRON_FURNACE_5_4": {
        "instruction": "Collect 5 pieces of iron and place 4 furnaces.",
        "instruction_paraphrases": [
            "Gather 5 parts of iron and position 4 kilns.",
            "While you assemble 5 partitions of iron, you should also allocate 4 stoves in their places.",
            "As you amass 5 segments of iron, simultaneously establish 4 ovens at their respective positions.",
            "Procure thou five fragments of sturdy iron, and set forth four hearths of flame upon thy dwelling.",
            "Find within your grasp five shards of the ancient iron, and gently settle four earth-bound forges."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.IRON, BlockType.FURNACE, 5, 4),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_DIAMOND_PLANT_2_3": {
        "instruction": "Collect 2 Diamonds and place 3 Plants.",
        "instruction_paraphrases": [
            "Amass 2 gems and position 3 flora.",
            "By gathering a pair of diamonds then carefully situating three plants.",
            "Acquire a pair of precious stones and carefully locate three green lives in a complex setup.",
            "Procure thou, two jewels of inimitable shimmer and anchor three seedlings deeply rooted in loamy soil, I beseech thee.",
            "Within the world's immense silence, gather two stars fallen to earth and nestle three breaths of green close to your heart."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.PLANT, 2, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_STONE_CRAFTING_TABLE_4_4": {
        "instruction": "Collect 4 stones and use them to build 4 crafting tables.",
        "instruction_paraphrases": [
            "Gather 4 pebbles and utilize them to construct 4 workbenches.",
            "Four stones are required, with these you can assemble four crafting tables.",
            "Procure four rocks and employ them to erect four artisan platforms, maintaining the original intention.",
            "Garner thou a quartet of stones and, with them as thy tools, create a like number of tables to craft upon, in the manner of the old ways.",
            "Find within your surroundings four earthly stones, and with a purposeful heart, mold them into four crafting tables – each a testament to the world's boundless resources."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.STONE, BlockType.CRAFTING_TABLE, 4, 4),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_COAL_CRAFTING_TABLE_3_3": {
        "instruction": "Gather 3 pieces of coal and set up 3 crafting tables.",
        "instruction_paraphrases": [
            "Collect three fragments of carbon and establish three workstations.",
            "Assemble the trio of carbon pieces all the while preparing three individual artisan spaces.",
            "Compile triad of carbon fragments whilst organizing a triplet of artisan platforms.",
            "In the heart of the stone-hewn chamber, bestow three fragments of the obsidian fire-stone, searing with dormant energy, and erect three tables of craftsmanship, hewn from the heartwood of elder trees.",
            "In the hidden realms of the earthborn fire-stone, quietly gather three fragments and, with gentle purpose, set forth three tables of craft, each imbued with a sense of creation and purpose."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.COAL, BlockType.CRAFTING_TABLE, 3, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_DIAMOND_PLANT_5_3": {
        "instruction": "Collect five diamonds and plant three saplings.",
        "instruction_paraphrases": [
            "Gather five gems and sow three seedlings.",
            "Acquisition of five resplendent diamonds is your primary task, followed by the cultivation of three young trees.",
            "Secure five precious stones and institute the growth of trio of young flora using a more complex linguistic structure.",
            "In your task lies the charge of assembling quintet of stars stolen from heaven's expanse, and bestow life to triple progeny of the ancient forest in a manner as engaging as a tale spun by J.R.R. Tolkien.",
            "Ponder upon the quest of amassing five glints of hard brilliance, and the quiet nurturing of three newborn whispers of the forest in the manner of Ursula K. Le Guin."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.PLANT, 5, 3),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    },
    "INSTRUCTION_PLACE_SAPLING_PLANT_3_1": {
        "instruction": "Collect 3 saplings and place 1 plant.",
        "instruction_paraphrases": [
            "Gather three young trees and position one flora.",
            "With three saplings collected, make it a point to establish one plant.",
            "Acquiring trio of young trees, you should orchestrate a single flora with resoluteness.",
            "Seek ye now three saplings, plucked from the earth's bounty, and shall a single sprout be bestowed within a chosen locale.",
            "With gentle hand, gather three newborn trees to you, then take one sprout of the old and grant it new roots."
        ],
        "scenario_checker": Scenarios.CONDITIONAL_PLACING,
        "arguments": create_target_state(InventoryItems.SAPLING, BlockType.PLANT, 3, 1),
        "str_check_lambda": "conditional_placing(game_data, ix)"
    }
}


# TODO: need to check how many synonyms are used

medium_test_other_paramets = {
  "INSTRUCTION_PLACE_COAL_PLANT_1_4": {
    "instruction": "Collect one lump of coal and then put down four shrubs.",
    "instruction_paraphrases": [
      "Get a bit of coal and set out four plants.",
      "Procure single black stone and place quartet of vegetation.",
      "Gather a piece of mineral coal and establish four greenery.",
      "Acquire one charcoal block and position four flora.",
      "Secure a solitary chunk of anthracite and layout four green plants."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.COAL, BlockType.PLANT, 1, 4),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_WOOD_STONE_3_2": {
    "instruction": "Collect 3 timber logs and place 2 boulders.",
    "instruction_paraphrases": [
      "Gather a trio of logs and situate a pair of rocks.",
      "You need to amass three units of lumber and establish two stones on the ground.",
      "I need you to acquire triple pieces of wood and then deposit dual pebbles.",
      "Procure three portions of timber and thereafter position a couple of rocks.",
      "Amass a total of three logs from the woods and correspondingly arrange exactly two stones."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.WOOD, BlockType.STONE, 3, 2),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_IRON_CRAFTING_TABLE_4_3": {
    "instruction": "Collect four pieces of iron and place down three crafting tables.",
    "instruction_paraphrases": [
      "Gather up four iron minerals and establish three workshops.",
      "Harvest four iron ore and set up three workbenches.",
      "Accumulate four metal iron and deploy three crafting stations.",
      "Procure four lumps of iron and erect three assembly tables.",
      "Amass four chunks of iron and install three fabrication benches."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.IRON, BlockType.CRAFTING_TABLE, 4, 3),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_DIAMOND_CRAFTING_TABLE_2_1": {
    "instruction": "Collect 2 diamonds and place 1 crafting table.",
    "instruction_paraphrases": [
      "Gather a pair of diamonds and put down a workbench.",
      "Acquire two pieces of diamond and situate one crafting table.",
      "Pocket dual gemstones and position a single making desk.",
      "Secure duo shine stones and establish one creation stand.",
      "Procure two units of the hardest mineral and install a solitary production bench."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.CRAFTING_TABLE, 2, 1),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_DIAMOND_PLANT_3_2": {
    "instruction": "Collect 3 diamonds and place 2 plants.",
    "instruction_paraphrases": [
      "Pick up 3 gemstones and after that put down a couple of shrubs.",
      "Secure 3 precious rocks and then proceed to position two vegetation.",
      "You must gather triple gemstones and then install two flora in the field.",
      "Procure the trio of precious stones and subsequently deposit a duo of vegetation in the area.",
      "After accumulating a trifecta of precious jewels, conspicuously plant a pair of greenery onto the landscape."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.PLANT, 3, 2),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_SAPLING_CRAFTING_TABLE_1_5": {
    "instruction": "Collect one sapling and place five crafting tables.",
    "instruction_paraphrases": [
      "Gather a sapling and erect five workbenches.",
      "Harvest a young tree and set up five furniture for crafting.",
      "Pick a sprout and put down five tables specifically for crafting.",
      "Procure a shoot and establish five crafting tables.",
      "Obtain a sapling and position five crafting tables."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.SAPLING, BlockType.CRAFTING_TABLE, 1, 5),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_IRON_STONE_1_4": {
    "instruction": "Collect one piece of Iron and then place four pieces of Stone.",
    "instruction_paraphrases": [
      "Acquire one Iron and subsequently lay four pieces of Rock.",
      "Secure one unit of Iron and then proceed to install four Stones.",
      "Grab one Iron item and follow it up by situating four pieces of Stone.",
      "Procure one iron unit and afterwards position four Stone entities.",
      "Furniture one Iron item and then subsequently deposit four Rocks."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.IRON, BlockType.STONE, 1, 4),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_IRON_FURNACE_4_5": {
    "instruction": "Gather 4 pieces of iron and place 5 units of furnace.",
    "instruction_paraphrases": [
      "Procure 4 iron ores then set up 5 furnaces.",
      "Acquire 4 chunks of iron and install 5 heating systems.",
      "Collect quadruple iron and erect 5 cooking stoves on the map.",
      "Earmark 4 iron nuggets for collection and station 5 charcoal grills.",
      "Secure a quartet of iron nodes and station 5 kilns."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.IRON, BlockType.FURNACE, 4, 5),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_STONE_FURNACE_5_5": {
    "instruction": "Collect 5 Stone and place 5 Furnace.",
    "instruction_paraphrases": [
      "Gather 5 pieces of Rock material and set up 5 Ovens.",
      "Acquire a collection of 5 Stones and establish 5 Furnaces.",
      "Amass 5 Stone items and install 5 heating devices.",
      "Accumulate 5 quarry products and put in place 5 stoves.",
      "Procure 5 units of Stone resource and deploy 5 fireboxes."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.STONE, BlockType.FURNACE, 5, 5),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_WOOD_STONE_2_2": {
    "instruction": "Collect two pieces of wood and then place two stones.",
    "instruction_paraphrases": [
      "Gather up two logs and follow that by placing down two rocks.",
      "Ensure you've picked up a pair of wood and subsequently locate two stones on the terrain.",
      "Start by obtaining two units of timber, then proceed to lay two pieces of stone.",
      "Secure for yourself a duo of wood and succeed that action by situating a couple of stones.",
      "Accumulate two fragments of lumber, then arrange a set of two stones."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.WOOD, BlockType.STONE, 2, 2),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_SAPLING_FURNACE_3_3": {
    "instruction": "Collect three saplings and place three furnaces.",
    "instruction_paraphrases": [
      "Gather a trio of saplings and set down the same number of furnaces.",
      "Secure three saplings from the environment and subsequently, establish three ovens.",
      "Harvest three saplings from the environment and proceed to set down an equivalent number of stoves.",
      "Accumulate three individual sapling items and additionally position three fireboxes into the area.",
      "From the surroundings, remove three saplings and later, lay down a trio of heating units."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.SAPLING, BlockType.FURNACE, 3, 3),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_COAL_STONE_4_4": {
    "instruction": "Collect 4 pieces of coal and place 4 blocks of stone.",
    "instruction_paraphrases": [
      "Find 4 coals and put down 4 stones on the map.",
      "Gather 4 applications of coal and deposit 4 applications of rock.",
      "Accumulate 4 units of coal and situate 4 units of stone.",
      "Amass a total of 4 coals and station a total of 4 stones.",
      "Assemble together 4 chunks of coal, then assort 4 pieces of stone."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.COAL, BlockType.STONE, 4, 4),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_WOOD_FURNACE_4_3": {
    "instruction": "Collect 4 pieces of wood and place 3 furnace units.",
    "instruction_paraphrases": [
      "Acquire 4 logs of wood and deploy 3 units of furnace.",
      "Make sure to gather a sum of four wooden pieces and install three times a furnace.",
      "The task requires you to obtain 4 units of timber and set up 3 furnaces.",
      "You have to pick up 4 planks of wood and put down 3 types of the furnace block.",
      "Amass a total of four bits of tree trunks and proceed to position three instances of the furnace structure."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.WOOD, BlockType.FURNACE, 4, 3),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_IRON_FURNACE_1_4": {
    "instruction": "Collect one piece of iron and place four furnaces.",
    "instruction_paraphrases": [
      "Get your hands on a single iron and put down four furnaces.",
      "Acquire one iron and set down four heating devices.",
      "Procure one piece of metallic element and establish four furnaces.",
      "Secure a single iron and position four pieces of heating machinery.",
      "Gather one iron and install four heating apparatus."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.IRON, BlockType.FURNACE, 1, 4),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_WOOD_CRAFTING_TABLE_3_5": {
    "instruction": "Collect 3 pieces of wood and place 5 crafting tables.",
    "instruction_paraphrases": [
      "Gather 3 wooden units and set up 5 crafting tables.",
      "Retrieve 3 logs of wood and construct 5 workbenches.",
      "Secure 3 timber blocks and establish 5 builder's platforms.",
      "Acquire 3 chunks of lumber and position 5 crafting stations.",
      "Procure 3 sections of timber and situate 5 artisan tables."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.WOOD, BlockType.CRAFTING_TABLE, 3, 5),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_DIAMOND_STONE_2_4": {
    "instruction": "Collect 2 diamonds and then place 4 stones.",
    "instruction_paraphrases": [
      "Gather 2 diamond gems and afterwards install 4 pieces of rock.",
      "Amass a pair of diamonds and then lay down four rocks.",
      "Assemble a duo of diamond jewels and subsequently set up four stones.",
      "Accumulate two diamond pieces and then deposit quartet of rocks.",
      "Accrue two units of diamond and following that, position four units of stone."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.STONE, 2, 4),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_STONE_STONE_2_5": {
    "instruction": "Collect 2 Stone and place 5 Stone.",
    "instruction_paraphrases": [
      "Gather a pair of Stones and then place a fistful of five Stones.",
      "Present me with two Rocks, followed by placing five of the Rocks.",
      "Accumulate 2 pieces of Stone then set down a total of five pieces of Stone.",
      "Amass a twosome of Stones and arrange quintet of them.",
      "Procure 2 Stones, following which exhibit an arrangement of 5 Stones."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.STONE, BlockType.STONE, 2, 5),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_SAPLING_FURNACE_3_2": {
    "instruction": "Gather 3 saplings and construct 2 furnaces.",
    "instruction_paraphrases": [
      "Collect three tree seedlings and build up two ovens.",
      "Procure trio of tree sprouts and erect a pair of kilns.",
      "Assemble three new growths from trees and put together two heating devices.",
      "Accumulate a set of three seedlings and establish a duo of stoves.",
      "Amass an amount of three tree saplings and fabricate two smelters."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.SAPLING, BlockType.FURNACE, 3, 2),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_DIAMOND_STONE_1_3": {
    "instruction": "Please collect one diamond and then find three rocks and place them down.",
    "instruction_paraphrases": [
      "Make sure to gather a diamond and after that, locate three stones to place on the ground.",
      "Obtain a single diamond from the environment, then your next task is to deposit a trio of rocks in this area.",
      "You need to get a diamond and then pick up three pieces of rock and deposit them.",
      "Your task is to get hold of a diamond and subsequently lay down three blocks of stone in this location.",
      "Procure one piece of diamond and then, arrange three pieces of stone on the landscape."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.STONE, 1, 3),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_DIAMOND_PLANT_1_4": {
    "instruction": "Gather one diamond and plant four saplings.",
    "instruction_paraphrases": [
      "Collect a gemstone and grow four trees.",
      "Procure a single diamond and sow four seeds.",
      "Acquire one piece of diamond and place in the ground four saplings.",
      "Obtain one specimen of diamond and position on the earth four young trees.",
      "Secure a unit of diamond and establish four juvenile flora on the map."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.DIAMOND, BlockType.PLANT, 1, 4),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  },
  "INSTRUCTION_PLACE_IRON_CRAFTING_TABLE_4_2": {
    "instruction": "Collect 4 iron pieces and place 2 crafting tables.",
    "instruction_paraphrases": [
      "Acquire four pieces of iron then put down a couple of crafting workbenches.",
      "You need to gather quartet of iron elements and lay two crafting platforms out.",
      "The task is to accumulate four iron units and establish two fabrication tables.",
      "Must extract quadruplet iron items from the environment and construct two craft stations.",
      "Your mission is to procure a tetrad iron constituents and erect duo creation desks."
    ],
    "scenario_checker": Scenarios.CONDITIONAL_PLACING,
    "arguments": create_target_state(InventoryItems.IRON, BlockType.CRAFTING_TABLE, 4, 2),
    "str_check_lambda": "conditional_placing(game_data, ix)"
  }
}

hard_test_parafrased = {}

hard_test_other_paramets = {}
