from game import *
import unittest

a = Hero()
b = Villain()

class CharacterTesting:
    """

    Tests Character properties and default values

    """
    def __init__(self) -> None:
        return

    def testPlayerRead(self, char:Character, player:Player) -> bool:
        return char.player == player
    
    def testPlayerWrite(self, char:Character, player:Player) -> bool:
        if player == Player.HERO:
            char.player = Player.VILLAIN
            return char.player == Player.VILLAIN
        else:
            char.player = Player.HERO
            return char.player == Player.HERO
    
    def testPlayerWriteInt(self, char:Character) -> None:
        char.player = 10
    
    def testHealthRead(self, char:Character) -> bool:
        return char.health == 5
    
    def testHealthWrite(self, char:Character) -> bool:
        char.health = 10
        return char.health == 10
    
    def testHealthWriteNegative(self, char:Character) -> None:
        char.health = -10
    
    def testHealthWriteZero(self, char:Character) -> None:
        char.health = 0
    
    def testHealthWriteStr(self, char:Character) -> None:
        char.health = "Hello"
    
    def testTempHealthRead(self, char:Character) -> bool:
        return char.temp_health == 5
    
    def testTempHealthWrite(self, char:Character) -> bool:
        char.temp_health = 10
        return char.temp_health == 10
    
    def testTempHealthWriteNegative(self, char:Character) -> None:
        char.temp_health = -10
    
    def testTempHealthWriteZero(self, char:Character) -> bool:
        char.temp_health = 0
        return char.temp_health == 0
    
    def testCharacterDeathTempHealthReset(self, char:Character) -> bool:
        try:
            char.temp_health = -5
        except:
            return char.temp_health == 0
        return
    
    def testTempHealthWriteStr(self, char:Character) -> None:
        char.temp_health = "Hello"
    
    def testAttackWrite(self, char:Character) -> bool:
        pass

class HeroTesting(unittest.TestCase):
    """

    Tests Hero Method implementations, properties, and Child Class method changes

    """
    def testHeroPlayerProperty(self) -> None:
        c = CharacterTesting()
        self.assertTrue(c.testPlayerRead(Hero(), Player.HERO))
        self.assertTrue(c.testPlayerWrite(Hero(), Player.HERO))
        with self.assertRaises(TypeError):
            c.testPlayerWriteInt(Hero())
    
    def testHeroHealthProperty(self) -> None:
        c = CharacterTesting()
        self.assertTrue(c.testHealthRead(Hero()))
        self.assertTrue(c.testHealthWrite(Hero()))
        with self.assertRaises(ValueError):
            c.testHealthWriteNegative(Hero())
        with self.assertRaises(ValueError):
            c.testHealthWriteZero(Hero())
        with self.assertRaises(TypeError):
            c.testHealthWriteStr(Hero())
    
    def testTempHealthProperty(self) -> None:
        c = CharacterTesting()
        self.assertTrue(c.testTempHealthRead(Hero()))
        self.assertTrue(c.testTempHealthWrite(Hero()))
        with self.assertRaises(CharacterDeath):
            c.testTempHealthWriteNegative(Hero())
        self.assertTrue(c.testTempHealthWriteZero(Hero()))
        self.assertTrue(c.testCharacterDeathTempHealthReset(Hero()))
        with self.assertRaises(TypeError):
            c.testTempHealthWriteStr(Hero())
    
    def testHeroStr(self) -> None:
        self.assertEqual(str(Hero()), "Hero")
        self.assertEqual(str(Warrior()), "Warrior")
        self.assertEqual(str(Mage()), "Mage")
        self.assertEqual(str(Paladin()), "Paladin")
        self.assertEqual(str(Ranger()), "Ranger")

class VillainTesting(unittest.TestCase):
    """

    Tests Villain Method implementations, properties, and Child Class method changes

    """
    def testVillainPlayerProperty(self) -> None:
        c = CharacterTesting()
        self.assertTrue(c.testPlayerRead(Villain(), Player.VILLAIN))
        self.assertTrue(c.testPlayerWrite(Villain(), Player.VILLAIN))
        with self.assertRaises(TypeError):
            c.testPlayerWriteInt(Villain())
    
    def testVillainHealthProperty(self) -> None:
        c = CharacterTesting()
        self.assertTrue(c.testHealthRead(Villain()))
        self.assertTrue(c.testHealthWrite(Villain()))
        with self.assertRaises(ValueError):
            c.testHealthWriteNegative(Villain())
        with self.assertRaises(ValueError):
            c.testHealthWriteZero(Villain())
        with self.assertRaises(TypeError):
            c.testHealthWriteStr(Villain())
    
    def testVillainStr(self) -> None:
        self.assertEqual(str(Villain()), "Villain")
        self.assertEqual(str(Goblin()), "Goblin")
        self.assertEqual(str(Skeleton()), "Skeleton")
        self.assertEqual(str(Necromancer()), "Necromancer")

class DungeonTesting(unittest.TestCase):
    """

    Tests Dungeon class properties and methods, as well as how it interacts with the character and creature

    """
    pass

if __name__ == "__main__":
    unittest.main()