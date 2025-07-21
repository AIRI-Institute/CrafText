from enum import Enum
import os
from flax import struct
from pathlib import Path

current_path = Path(__file__)
craftext_root = current_path.parent.parent
plans_path = os.path.join(craftext_root, "dataset", "scenarious", "extra_files", "easy_gpt4_action_plans.json")

@struct.dataclass
class AchievementState:
    NOT_MATTER = 0
    NEED_TO_ACHIEVE = 1
    AVOID_TO_ACHIEVE = -1
    
@struct.dataclass
class Scenarios:
    CONDITIONAL_ACHIEVEMENTS = 0
    CONDITIONAL_PLACING = 1
    LOCALIZATION_PLACE = 2
    
    BUILD_LINE = 3
    BUILD_SQUARE = 4
    BUILD_STAR = 5
    
    TIME_CONSTRAINED_PLACEMENT = 6
    EXPLORE = 7
    
@struct.dataclass    
class MediumInventoryItems:
    WOOD = 0
    STONE = 1
    COAL = 2
    IRON = 3
    DIAMOND = 4
    SAPLING = 5
    PICKAXE = 6
    SWORD = 7
    BOW = 8
    ARROWS = 9
    ARMOUR = 10
    TORCHES = 11
    RUBY = 12
    SAPPHIRE = 13
    POTIONS = 14
    BOOKS = 15

@struct.dataclass
class Achievement:
    COLLECT_WOOD = 0
    PLACE_TABLE = 1
    EAT_COW = 2
    COLLECT_SAPLING = 3
    COLLECT_DRINK = 4
    MAKE_WOOD_PICKAXE = 5
    MAKE_WOOD_SWORD = 6
    PLACE_PLANT = 7
    DEFEAT_ZOMBIE = 8
    COLLECT_STONE = 9
    PLACE_STONE = 10
    EAT_PLANT = 11
    DEFEAT_SKELETON = 12
    MAKE_STONE_PICKAXE = 13
    MAKE_STONE_SWORD = 14
    WAKE_UP = 15
    PLACE_FURNACE = 16
    COLLECT_COAL = 17
    COLLECT_IRON = 18
    COLLECT_DIAMOND = 19
    MAKE_IRON_PICKAXE = 20
    MAKE_IRON_SWORD = 21

    MAKE_ARROW = 22
    MAKE_TORCH = 23
    PLACE_TORCH = 24

    COLLECT_SAPPHIRE = 54
    COLLECT_RUBY = 59
    MAKE_DIAMOND_PICKAXE = 60
    MAKE_DIAMOND_SWORD = 25
    MAKE_IRON_ARMOUR = 26
    MAKE_DIAMOND_ARMOUR = 27

    ENTER_GNOMISH_MINES = 28
    ENTER_DUNGEON = 29
    ENTER_SEWERS = 30
    ENTER_VAULT = 31
    ENTER_TROLL_MINES = 32
    ENTER_FIRE_REALM = 33
    ENTER_ICE_REALM = 34
    ENTER_GRAVEYARD = 35

    DEFEAT_GNOME_WARRIOR = 36
    DEFEAT_GNOME_ARCHER = 37
    DEFEAT_ORC_SOLIDER = 38
    DEFEAT_ORC_MAGE = 39
    DEFEAT_LIZARD = 40
    DEFEAT_KOBOLD = 41
    DEFEAT_KNIGHT = 65
    DEFEAT_ARCHER = 66
    DEFEAT_TROLL = 42
    DEFEAT_DEEP_THING = 43
    DEFEAT_PIGMAN = 44
    DEFEAT_FIRE_ELEMENTAL = 45
    DEFEAT_FROST_TROLL = 46
    DEFEAT_ICE_ELEMENTAL = 47
    DAMAGE_NECROMANCER = 48
    DEFEAT_NECROMANCER = 49

    EAT_BAT = 50
    EAT_SNAIL = 51

    FIND_BOW = 52
    FIRE_BOW = 53

    LEARN_FIREBALL = 55
    CAST_FIREBALL = 56
    LEARN_ICEBALL = 57
    CAST_ICEBALL = 58

    OPEN_CHEST = 61
    DRINK_POTION = 62
    ENCHANT_SWORD = 63
    ENCHANT_ARMOUR = 64
    SMTH = 65
    END = 66

@struct.dataclass
class InventoryItems:
    WOOD = 0
    STONE = 1
    COAL = 2
    IRON = 3
    DIAMOND = 4
    SAPLING = 5
    WOOD_PICKAXE = 6
    STONE_PICKAXE = 7
    IRON_PICKAXE = 8
    WOOD_SWORD = 9
    STONE_SWORD = 10
    IRON_SWORD = 11
 

@struct.dataclass
class BlockType:
    INVALID = 0
    OUT_OF_BOUNDS = 1
    GRASS = 2
    WATER = 3
    STONE = 4
    TREE = 5
    WOOD = 6
    PATH = 7
    COAL = 8
    IRON = 9
    DIAMOND = 10
    CRAFTING_TABLE = 11
    FURNACE = 12
    SAND = 13
    LAVA = 14
    PLANT = 15
    RIPE_PLANT = 16
    WALL = 17
    DARKNESS = 18
    WALL_MOSS = 19
    STALAGMITE = 20
    SAPPHIRE = 21
    RUBY = 22
    CHEST = 23
    FOUNTAIN = 24
    FIRE_GRASS = 25
    ICE_GRASS = 26
    GRAVEL = 27
    FIRE_TREE = 28
    ICE_SHRUB = 29
    ENCHANTMENT_TABLE_FIRE = 30
    ENCHANTMENT_TABLE_ICE = 31
    NECROMANCER = 32
    GRAVE = 33
    GRAVE2 = 34
    GRAVE3 = 35
    NECROMANCER_VULNERABLE = 36
    
@struct.dataclass
class TimeState:
    NIGHT = 0
    MORNING = 1
    EVENING = 2
    DAY = 3


@struct.dataclass
class CrossType:
    STRAIGHT = 0
    DIAGONAL = 1
    COMBINED = 2