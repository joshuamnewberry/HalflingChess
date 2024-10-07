from character import *

class Villain(Character):
    def __init__(self) -> None:
        super().__init__(Player.VILLAIN)
    
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        pass
    
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board:List[List[None|Character]]) -> bool:
        pass
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], *args, **kwargs) -> int:
        pass

    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        pass

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

class Heroes(Character):
    def __init__(self) -> None:
        super().__init__(Player.HERO)
    
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        pass
    
    def is_valid_attack(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        pass
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], *args, **kwargs) -> int:
        pass

    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        pass

class Warrior(Heroes):
    def __init__(self) -> None:
        super().__init__()
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]
    
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = [], gob:list = []) -> None:
        pass

class Mage(Heroes):
    def __init__(self) -> None:
        super().__init__()
        self.combat = [2, 2]
        self.range = 3
        self.move = 2
    
    def deal_damage(self, target:Character, damage:int):
        pass

class Paladin(Heroes):
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

class Ranger(Heroes):
    def __init__(self) -> None:
        super().__init__()
        self.range = 3
    
    def deal_damage(self, target:Character, damage:int):
        pass
