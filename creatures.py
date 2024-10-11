from character import *

class Villain(Character):
    def __init__(self) -> None:
        super().__init__(Player.VILLAIN)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        if super().is_valid_move(from_coord, to_coord, board):
            if from_coord.x == to_coord.x or from_coord.y == from_coord.y:
                return True
        return False
    
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board:List[List[None|Character]]) -> bool:
        if super().is_valid_attack(from_coord, to_coord, board):
            if from_coord.x == to_coord.x or from_coord.y == from_coord.y:
                return True
        return False
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], *args, **kwargs) -> int:
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        super().deal_damage(target, damage)

class Goblin(Villain):
    def __init__(self) -> None:
        super().__init__()
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]

class Skeleton(Villain):
    def __init__(self) -> None:
        super().__init__()
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2

class Necromancer(Villain):
    def __init__(self) -> None:
        super().__init__()
        self.combat = [1, 2]
        self.range = 3
    
    def raise_dead(target:Character) -> None:
        target.player = Player.VILLAIN
        target.temp_health = int(target.health / 2)

class Hero(Character):
    def __init__(self) -> None:
        super().__init__(Player.HERO)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        return super().is_valid_move(from_coord, to_coord, board)
    
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board:List[List[None|Character]]) -> bool:
        return super().is_valid_attack(from_coord, to_coord, board)
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], *args, **kwargs) -> int:
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        super().deal_damage(target, damage)

class Warrior(Hero):
    def __init__(self) -> None:
        super().__init__()
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], gob:list = []) -> int:
        if target.__class__ == Goblin:
            if len(gob) == 0:
                return super().calculate_dice(target, attack+2, list)
            num = 0
            compare = 3
            if attack:
                compare = 4
            if gob[0] > compare:
                num += 1
            if gob[1] > compare:
                num += 1
            return super().calculate_dice(target, attack, list) + num

class Mage(Hero):
    def __init__(self) -> None:
        super().__init__()
        self.combat = [2, 2]
        self.range = 3
        self.move = 2
    
    def deal_damage(self, target:Character, damage:int):
        super().deal_damage(target, damage + 1)

class Paladin(Hero):
    def __init__(self) -> None:
        super().__init__()
        self.__heal = True
        self.health = 6
        self.temp_health = 6
    
    @property
    def heal(self) -> bool:
        return self.__heal
    @heal.setter
    def heal(self, heal) -> None:
        if type(heal) != bool:
            raise TypeError
        self.__heal = heal
    
    def revive(self, target:Character) -> None:
        if self.__heal:
            target.temp_health = int(target.health / 2)
            self.__heal = False

class Ranger(Hero):
    def __init__(self) -> None:
        super().__init__()
        self.range = 3
    
    def deal_damage(self, target:Character, damage:int) -> None:
        if target.__class__ == Skeleton:
            return super().deal_damage(target, damage-1)
        return super().deal_damage(target, damage)
