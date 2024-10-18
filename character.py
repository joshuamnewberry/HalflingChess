from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any
from enum import Enum
from random import randint
from coord import Coord

class CharacterDeath(Exception):
    """

    Custom Exception for Character Deaths

    """

    def __init__(self, msg:str, char:Character) -> None:
        """
        Initialize the object, store the message and set the character's temp health back to zero

        Parameters:
        msg:str the message to be printed
        char:Character the character who died, their temp_health will be set to zero

        Return:
        None

        """
        self.message = msg
        char.temp_health = 0
    
    def __str__(self) -> str:
        """
        Return the message

        Parameters:
        None

        Return:
        self.message:str The stored message

        """
        return self.message

class Player(Enum):
    """
    Enumerator class used to denote Player association

    """
    VILLAIN = 0
    HERO = 1

class Character(ABC):
    def __init__(self, player:Player) -> None:
        """
        Initialize the object, check player is type Player and store initial variable values
        
        Parameters:
        player:Player Player type of the Character (Hero or Villain)

        Return:
        None

        """
        if type(player) != Player:
            raise TypeError
        self.__player = player
        self.__health = 5
        self.__temp_health = 5
        self.__attack = 3
        self.__defense = 3
        self.__move = 3
        self.__range = 1
    
    def __str__(self) -> str:
        """
        Return the Class name

        Parameters:
        None

        Return:
        self.__class__.__name__:str the class name of the object
        
        """
        return self.__class__.__name__
    
    def integerType(self, num:Any) -> None:
        """
        Raise a TypeError if num is not an Integer

        Parameters:
        num:Any 

        Return:
        None

        """
        if type(num) != int:
            raise TypeError
    
    @property
    def player(self) -> Player:
        """
        Get or Set player variable

        Parameters:
        player:Player if passed will be the new player type

        Return:
        self.__player if getting will return player type

        """
        return self.__player
    @player.setter
    def player(self, player:Player) -> None:
        if type(player) != Player:
            raise TypeError
        self.__player = player
    
    @property
    def health(self) -> int:
        """
        Get or Set health variable, check int type and greater than 0

        Parameters:
        health:int if passed will be the new health

        Return:
        self.__health if getting will return health

        """
        return self.__health
    @health.setter
    def health(self, health:int) -> None:
        self.integerType(health)
        if health <= 0:
            raise ValueError
        self.__health = health
    
    @property
    def temp_health(self) -> int:
        """
        Get or Set temp_health variable, check int type, if less than zero raise CharacterDeath exception

        Parameters:
        temp_health:int if passed will be the new temp_health

        Return:
        self.__temp_health if getting will return temp_health

        """
        return self.__temp_health
    @temp_health.setter
    def temp_health(self, temp_health:int) -> None:
        self.integerType(temp_health)
        self.__temp_health = temp_health
        if self.__temp_health < 0:
            raise CharacterDeath(f"{self} has died", self)
    
    @property
    def combat(self) -> list:
        """
        Get or Set attack and defense variables, check int type, length of 2, greater than or equal to 0

        Parameters:
        combat:list if passed will set the new attacka and defense values

        Return:
        [self.__attack, self.__defense] will return attack and defense variables in a list of length 2

        """
        return [self.__attack, self.__defense]
    @combat.setter
    def combat(self, combat:list) -> None:
        if type(combat) != list:
            raise TypeError
        if len(combat) != 2:
            raise ValueError
        self.integerType(combat[0])
        self.integerType(combat[1])
        if combat[0] < 0 or combat[1] < 0:
            raise ValueError
        self.__attack = combat[0]
        self.__defense = combat[1]
    
    @property
    def move(self) -> int:
        """
        Get or Set move variable, check int type, greater than 0

        Parameters:
        move:int if passed will be the new move value

        Return:
        self.__move if getting will return move

        """
        return self.__move
    @move.setter
    def move(self, move:int) -> None:
        self.integerType(move)
        if move <= 0:
            raise ValueError
        self.__move = move
    
    @property
    def range(self) -> int:
        """
        Get or Set range variable, check int type, greater than 0

        Parameters:
        range:int if passed will be the new range value

        Return:
        self.__range if getting will return range

        """
        return self.__range
    @range.setter
    def range(self, range:int) -> None:
        self.integerType(range)
        if range <= 0:
            raise ValueError
        self.__range = range
    
    @abstractmethod
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
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        height = len(board)-1
        width = len(board[0])-1
        if from_coord.x < 0 or to_coord.x < 0 or from_coord.y < 0 or to_coord.y < 0:
            return False
        if from_coord.x > height or to_coord.x > height or from_coord.y > width or to_coord.y > width:
            return False
        if board[from_coord.x][from_coord.y] != self:
            return False
        if board[to_coord.x][to_coord.y] != None:
            return False
        return True
    
    @abstractmethod
    def is_valid_attack(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the attack is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        height = len(board)-1
        width = len(board[0])-1
        if from_coord.x < 0 or to_coord.x < 0 or from_coord.y < 0 or to_coord.y < 0:
            return False
        if from_coord.x > height or to_coord.x > height or from_coord.y > width or to_coord.y > width:
            return False
        if board[from_coord.x][from_coord.y] != self:
            return False
        if not isinstance(board[to_coord.x][to_coord.y], Character):
            return False
        return True
    
    @abstractmethod
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = None, *args, **kwargs) -> int:
        """
        Returns the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        sucess_num: int number of sucessful rolls
        
        """
        if lst is None:
            lst = []
        sucess_num = 0
        dice_num = self.combat[int(not attack)]
        compare = 3
        if attack:
            compare = 4
        if lst == []:
            for _ in range(1, dice_num):
                lst.append(randint(1, 6))
        for i in range(0, self.__attack-1):
            if lst[i] > compare:
                sucess_num += 1
        return sucess_num
    
    @abstractmethod
    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        """
        Modify 

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        sucess_num: int number of sucessful rolls
        
        """
        print(f"{target.__class__.__name__} was dealt {damage} damage")
        try:
            target.__temp_health -= damage
        except CharacterDeath as msg:
           
            print(msg)