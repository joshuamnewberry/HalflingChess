from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from random import randint
from coord import Coord

class CharacterDeath(Exception):
    def __init__(self, msg:str, char:Character) -> None:
        self.message = msg
        self.char = char
    
    def __str__(self) -> str:
        return ""

class Player(Enum):
    VILLAIN = 0
    HERO = 1

class Character(ABC):
    def __init__(self, player:Player) -> None:
        if type(player) != Player:
            raise TypeError
        self.__player = player
        self.__health = 5
        self.__temp_health = 5
        self.__attack = 3
        self.__defense = 3
        self.__move = 3
        self.__range = 1
    
    @abstractmethod
    def __str__(self) -> str:
        return self.__class__.__name__
    
    def integerType(num) -> None:
        if type(num) != int:
            raise TypeError
    
    @property
    def player(self) -> Player:
        return self.__player
    @player.setter
    def player(self, player:Player) -> None:
        if type(player) != Player:
            raise TypeError
        self.__player = player
    
    @property
    def health(self) -> int:
        return self.__health
    @health.setter
    def health(self, health:int) -> None:
        Character.integerType(health)
        if health <= 0:
            raise ValueError
        self.__health = health
    
    @property
    def temp_health(self) -> int:
        return self.__temp_health
    @player.setter
    def temp_health(self, temp_health:int) -> None:
        Character.integerType(temp_health)
        self.__temp_health = temp_health
        if self.__temp_health < 0:
            raise CharacterDeath
    
    @property
    def combat(self) -> list:
        return [self.__attack, self.__defense]
    @combat.setter
    def combat(self, combat:list) -> None:
        Character.integerType(combat[0])
        Character.integerType(combat[1])
        if combat[0] < 0 or combat[1] < 0:
            raise ValueError
        self.__attack = combat[0]
        self.__defense = combat[1]
    
    @property
    def move(self) -> int:
        return self.__move
    @move.setter
    def move(self, move:int) -> None:
        self.integerType()
        if move <= 0:
            raise ValueError
        self.__move = move
    
    @property
    def range(self) -> int:
        return self.__range
    @range.setter
    def range(self, range:int) -> None:
        self.integerType(range)
        if range <= 0:
            raise ValueError
        self.__range = range
    
    @abstractmethod
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        height = len(board)
        width = len(board[0])
        if from_coord.x < 0 or to_coord.x < 0 or from_coord.y < 0 or to_coord.y < 0:
            return False
        if from_coord.x > width or to_coord.x > width or from_coord.y > height or to_coord.y > height:
            return False
        if board[from_coord.x][from_coord.y] != self:
            return False
        if board[to_coord.x][to_coord.y] != None:
            return False
        return True
    
    @abstractmethod
    def is_valid_attack(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        height = len(board)
        width = len(board[0])
        if from_coord.x < 0 or to_coord.x < 0 or from_coord.y < 0 or to_coord.y < 0:
            return False
        if from_coord.x > width or to_coord.x > width or from_coord.y > height or to_coord.y > height:
            return False
        if board[from_coord.x][from_coord.y] != self:
            return False
        if not isinstance(board[to_coord.x][to_coord.y], Character):
            return False
        return True
    
    @abstractmethod
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], *args, **kwargs) -> int:
        num = 0
        compare = 3
        if attack:
            compare = 4
        if lst == []:
            for i in range(1, attack):
                if randint(1, 6) > compare:
                    num += 1
        else:
            for i in lst:
                if i > compare:
                    num += 1
        return num

    @abstractmethod
    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        print(f"{target.__class__.__name__} was dealt {damage} damage")
        try:
            target.__temp_health -= damage
        except CharacterDeath as msg:
            print(msg)
