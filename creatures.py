from character import *

class Villain(Character):
    def __init__(self) -> None:
        """
        Initialize the object with Player type Player.VILLAIN

        Parameters:
        None

        Return:
        None

        """
        super().__init__(Player.VILLAIN)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the move is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """
        if super().is_valid_move(from_coord, to_coord, board):
            if abs(to_coord.x - from_coord.x) <= self.move and abs(to_coord.y - from_coord.y) <= self.move:
                if from_coord.x == to_coord.x:
                    for y in range (min(from_coord.y, to_coord.y) + 1, max(from_coord.y, to_coord.y)):
                        if board[from_coord.x][y] != None:
                            return False
                    return True
                if from_coord.y == to_coord.y:
                    for x in range (min(from_coord.x, to_coord.x) + 1, max(from_coord.x, to_coord.x)):
                        if board[x][from_coord.y] != None:
                            return False
                    return True
        return False
    
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the attack is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the target
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """
        if super().is_valid_attack(from_coord, to_coord, board):
            if from_coord.x == to_coord.x or from_coord.y == from_coord.y:
                if abs(to_coord.x - from_coord.x) <= self.range and abs(to_coord.y - from_coord.y) <= self.range:
                    return True
        return False
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = None, *args, **kwargs) -> int:
        """
        Return the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num:int number of sucessful rolls
        
        """
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        """
        Subtract damage from target.temp_health and print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None
        
        """
        super().deal_damage(target, damage)

class Goblin(Villain):
    def __init__(self) -> None:
        """
        Initialize the object as a Villain, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]

class Skeleton(Villain):
    def __init__(self) -> None:
        """
        Initialize the object as a Villain, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2

class Necromancer(Villain):
    def __init__(self) -> None:
        """
        Initialize the object as a Villain, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.combat = [1, 2]
        self.range = 3
    
    def raise_dead(self, target:Character, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> None:
        """
        Check prereqs, and set player type to Player.VILLAIN and temp.health to health/2 rounded down

        Parameters:
        target:Character the Character getting raised from the dead
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        None

        """
        if target.temp_health != 0 or not self.is_valid_attack(from_coord, to_coord, board):
            return
        target.player = Player.VILLAIN
        target.temp_health = int(target.health / 2)

class Hero(Character):
    def __init__(self) -> None:
        """
        Initialize the object with Player type Player.HERO

        Parameters:
        None

        Return:
        None

        """
        super().__init__(Player.HERO)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the move is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """
        if super().is_valid_move(from_coord, to_coord, board):
            if abs(to_coord.x - from_coord.x) <= self.move and abs(to_coord.y - from_coord.y) <= self.move:
                return True
        return False
    
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the attack is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the target
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """
        if super().is_valid_attack(from_coord, to_coord, board):
            if abs(to_coord.x - from_coord.x) <= self.range and abs(to_coord.y - from_coord.y) <= self.range:
                return True
        return False
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = None, *args, **kwargs) -> int:
        """
        Return the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num:int number of sucessful rolls
        
        """
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        """
        Subtract damage from target.temp_health and print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None
        
        """
        super().deal_damage(target, damage)

class Warrior(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = None, gob:list = None) -> int:
        """
        Return the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6, also uses gob to roll 2 extra dice when
        attacking a goblin, or if empty generates 2 more rolls

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num: int number of sucessful rolls
        
        """
        sucess_num = 0
        if attack and target.__class__ == Goblin:
            if gob is None:
                gob = []
                for _ in range(0, 2):
                    gob.append(randint(1, 6))
            compare = 4
            for roll in gob:
                if roll > compare:
                    sucess_num += 1
        return super().calculate_dice(target, attack, lst) + sucess_num

class Mage(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.combat = [2, 2]
        self.range = 3
        self.move = 2
    
    def deal_damage(self, target:Character, damage:int):
        """
        Subtract damage from target.temp_health and print message if there is a Character Death, add 1 to damage for Mage class

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None
        
        """
        super().deal_damage(target, damage + 1)

class Paladin(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.__heal = True
        self.health = 6
        self.temp_health = 6
    
    @property
    def heal(self) -> bool:
        """
        Get or Set heal variable, check bool type

        Parameters:
        heal:bool if passed will be the new heal value

        Return:
        self.__heal if getting will return heal value

        """
        return self.__heal
    @heal.setter
    def heal(self, heal) -> None:
        if type(heal) != bool:
            raise TypeError
        self.__heal = heal
    
    def revive(self, target:Character, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> None:
        """
        Check prereqs, set temp.health to health/2 rounded down and heal to false

        Parameters:
        target:Character the Character getting raised from the dead
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        None

        """
        if not self.__heal or target.player != Player.HERO or target.temp_health != 0 or not self.is_valid_attack(from_coord, to_coord, board):
            return
        target.temp_health = int(target.health / 2)
        self.__heal = False

class Ranger(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return:
        None

        """
        super().__init__()
        self.range = 3
    
    def deal_damage(self, target:Character, damage:int) -> None:
        """
        Subtract damage from target.temp_health, do one less damage to skeletons. Print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None
        
        """
        if target.__class__ == Skeleton:
            super().deal_damage(target, damage-1)
            return
        super().deal_damage(target, damage)