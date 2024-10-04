from creatures import *
from coord import *

class Dungeon:
    def boardLength(num) -> None:
        if type(num) != int:
            raise TypeError
        if num < 4:
            raise ValueError

    def __init__(self, height:int, width:int, lst:list) -> None:
        Dungeon.boardLength(height)
        Dungeon.boardLength(width)
        self.__height = height
        self.__width = width
        self.__board:List[List[None|Character]] = [[0 for i in range(height)] for j in range(width)]
        self.__player:Player = Player.HERO
        self.__heroes:List[Hero] = []
        self.__villains:List[Villain] = []
    
    @property
    def height(self) -> int:
        return self.__height
    @height.setter
    def height(self, height:int) -> None:
        Dungeon.boardLength(height)
        self.__height = height
    
    @property
    def width(self) -> int:
        return self.__width
    @width.setter
    def width(self, width:int) -> None:
        Dungeon.boardLength(width)
        self.__width = width
    
    @property
    def board(self) -> List[List[None|Character]]:
        return self.__board
    @board.setter
    def board(self, board:List[List[None|Character]]) -> None:
        if type(board) != List[List[None|Character]]:
            raise TypeError
        self.__board = board
    
    @property
    def player(self) -> Player:
        return self.__player
    @player.setter
    def player(self, player:Player) -> None:
        if type(player) != Player:
            raise TypeError
        self.__player = player
    
    @property
    def heroes(self) -> List[Hero]:
        return self.__heroes
    @heroes.setter
    def heroes(self, heroes:List[Hero]) -> None:
        if type(heroes) != List[Hero]:
            raise TypeError
        self.__heroes = heroes
    
    @property
    def villains(self) -> List[Hero]:
        return self.__villains
    @villains.setter
    def villains(self, villains:List[Villain]) -> None:
        if type(villains) != List[Villain]:
            raise TypeError
        self.__villains = villains
    
    def is_valid_move(self, coords:List[Coord]) -> bool:
        pass

    def is_valid_attack(self, coords:List[Coord]) -> bool:
        pass

    def character_at(self, x:int, y:int) -> Character:
        pass

    def set_character_at(self, target:Character, x:int, y:int):
        pass

    def move(self, from_coord:Coord, to_coord:Coord):
        pass

    def attack(self, from_coords:Coord, to_coords:Coord): 
        pass

    def set_next_player(self) -> None:
        if self.__player == Player.HERO:
            self.__player = Player.VILLAIN
        else:
            self.__player = Player.HERO

    def print_board(self) -> None:
        st = ' \t'
        st += '_____' * len(self.board)
        st += '\n'
        for i in range(len(self.__board)):
            st += f'{i}\t'
            for j in range(len(self.__board[i])):
                if self.board[i][j] is None:
                    st += '|___|'
                else:
                    st += f'|{self.board[i][j].__class__.__name__[:3]}|'
            st += '\n'
        st += '\t'
        for i in range(len(self.board[0])):
            st += f'  {i}  '
        print(st)
    
    def is_dungeon_clear(self) -> bool:
        pass

    def adventurer_defeat(self) -> bool:
        pass

    def generate_villains(self) -> None:
        pass

    def place_heroes(self) -> None:
        pass

    def place_villains(self) -> None:
        pass

    def generate_new_board(self, height:int = -1, width:int = -1) -> None:
        pass