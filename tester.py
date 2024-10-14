from game import *
import unittest

a = Hero()
b = Villain()

class CharacterTesting(unittest.TestCase):
    """

    Tests Character properties and default values

    """

    def testPlayerRead(self):
        self.assertEqual(a.player, Player.HERO)
        self.assertEqual(b.player, Player.VILLAIN)
    
    def testPlayerWrite(self):
        c = Hero()
        c.player = Player.VILLAIN
        self.assertEqual(c.player, Player.VILLAIN)
    
    def testPlayerWriteTypeError(self):
        with self.assertRaises(TypeError):
            c = Hero()
            c.player = 1
    
    def testHealthRead(self):
        self.assertEqual(a.health, 5)
        self.assertEqual(b.health, 5)
    
    def testHealthWrite(self):
        c = Hero()
        c.health = 10
        self.assertEqual(c.player, 10)
    
    def testHealthWriteTypeError(self):
        with self.assertRaises(TypeError):
            c = Hero()
            c.health = "Hello"
    
    def testHealthWriteNegative(self):
        with self.assertRaises(ValueError):
            c = Hero()
            c.health = -1

class HeroTesting(unittest.TestCase):
    """

    Tests Hero Method implementations and Child Class method changes

    """
    pass

class VillainTesting(unittest.TestCase):
    """

    Tests Villain Method implementations and Child Class method changes

    """
    pass

class DungeonTesting(unittest.TestCase):
    """

    Tests Dungeon class properties and methods, as well as how it interacts with the character and creature

    """
    pass

if __name__ == "__main__":
    unittest.main()