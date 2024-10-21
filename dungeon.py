from creatures import *
from coord import *

class Dungeon:
    def boardLength(num) -> None:
        if type(num) != int:
            raise TypeError
        if num < 4:
            raise ValueError
        if num > 12:
            raise ValueError

    def __init__(self, height: int, width: int, villains: List[Villain] = []) -> None:
        Dungeon.boardLength(height)
        Dungeon.boardLength(width)
        self.__height = height
        self.__width = width
        self.__board: List[List[None | Character]] = [[0 for i in range(height)] for j in range(width)]
        self.__player: Player = Player.HERO
        self.__heroes: List[Hero] = [Warrior(), Mage(), Paladin(), Ranger()]
        if villains == []:
            self.__villains: List[Villain] = Dungeon.generate_villains()
        else:
            self.__villains: List[Villain] = villains

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        Dungeon.boardLength(height)
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        Dungeon.boardLength(width)
        self.__width = width

    @property
    def board(self) -> List[List[None | Character]]:
        return self.__board

    @board.setter
    def board(self, board: List[List[None | Character]]) -> None:
        if type(board) != List[List[None | Character]]:
            raise TypeError
        self.__board = board

    @property
    def player(self) -> Player:
        return self.__player

    @player.setter
    def player(self, player: Player) -> None:
        if type(player) != Player:
            raise TypeError
        self.__player = player

    @property
    def heroes(self) -> List[Hero]:
        return self.__heroes

    @heroes.setter
    def heroes(self, heroes: List[Hero]) -> None:
        if type(heroes) != List[Hero]:
            raise TypeError
        self.__heroes = heroes

    @property
    def villains(self) -> List[Hero]:
        return self.__villains

    @villains.setter
    def villains(self, villains: List[Villain]) -> None:
        if type(villains) != List[Villain]:
            raise TypeError
        self.__villains = villains

    def is_valid_move(self, coords: List[Coord]) -> bool:
        return self.board[coords[0]][coords[1]].is_valid_attack(coords[0], coords[1], self.board)

    def is_valid_attack(self, coords: List[Coord]) -> bool:
        return self.board[coords[0]][coords[1]].is_valid_attack(coords[0], coords[1], self.board)

    def character_at(self, x: int, y: int) -> Character:
        # Check the coordinates
        if x < 0 or x >= self.__height:
            raise IndexError(f"x {x} is out of bounds.")
        if y < 0 or y >= self.__width:
            raise IndexError(f"y {y} is out of bounds.")

        # Get the character
        character = self.__board[x][y]

        # Return the character
        if character is not None:
            return character
        else:
            raise ValueError(f"No character found at position ({x}, {y}).")

    def set_character_at(self, target: Character, x: int, y: int) -> None:
        # Check if in bounds
        if x < 0 or x >= self.__height:
            raise IndexError(f"x {x} is out of bounds.")
        if y < 0 or y >= self.__width:
            raise IndexError(f"y {y} is out of bounds.")

        # Place character
        self.__board[x][y] = target

    def move(self, from_coord: Coord, to_coord: Coord) -> None:
        # Check if in bounds
        if not (0 <= from_coord.x < self.__height and 0 <= from_coord.y < self.__width):
            raise IndexError(f"from coord ({from_coord.x}, {from_coord.y}) is out of bounds.")
        if not (0 <= to_coord.x < self.__height and 0 <= to_coord.y < self.__width):
            raise IndexError(f"to coord ({to_coord.x}, {to_coord.y}) is out of bounds.")

        # Check if a character is there
        character = self.__board[from_coord.x][from_coord.y]
        if character is None:
            raise ValueError(f"No character at from coord ({from_coord.x}, {from_coord.y}) to move.")

        # Move the character
        self.__board[to_coord.x][to_coord.y] = character

        # Clear the original position
        self.__board[from_coord.x][from_coord.y] = None

    def attack(self, from_coords: Coord, to_coords: Coord) -> None:
        # Check if valid
        if not self.is_valid_attack([from_coords.x, from_coords.y]):
            print(f"Invalid attack move from ({from_coords.x}, {from_coords.y}) to ({to_coords.x}, {to_coords.y})")
            return

        # Get attacker and defender
        attacker = self.board[from_coords.x][from_coords.y]
        defender = self.board[to_coords.x][to_coords.y]

        if not attacker or not defender:
            print("No character present at one of the coordinates.")
            return

        # Get damage
        damage = attacker.calculate_damage(defender)

        # Apply damage
        if damage > 0:
            defender.temp_health -= damage
            print(f"{defender.__class__.__name__} took {damage} damage from {attacker.__class__.__name__}")
        else:
            print(f"{defender.__class__.__name__} took no damage from {attacker.__class__.__name__}")

        # Check if the defender was defeated
        if defender.temp_health <= 0:
            print(f"{defender.__class__.__name__} has been defeated!")

        # Set the next player
        self.set_next_player()

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
        for villain in self.villains:
            if villain.temp_health != 0:
                return False
        return True

    def adventurer_defeat(self) -> bool:
        for hero in self.heroes:
            if hero.temp_health != 0:
                return False
        return True

    def generate_villains(self) -> None:
        num_villains = random.randint(1, max(self.height, self.width))
        self.__villains = []  # Reset the villains list
        necromancer_added = False  # necromancer tracker

        for i in range(num_villains):
            roll = random.randint(1, 10)
            if 1 <= roll <= 5:  # 50% chance for Goblin
                self.__villains.append("Goblin")
            elif 6 <= roll <= 8:  # 30% chance for Skeleton
                self.__villains.append("Skeleton")
            elif 9 <= roll <= 10:  # 20% chance for Necromancer
                if necromancer_added:
                    self.__villains.append("Skeleton")  # Add a Skeleton instead
                else:
                    self.__villains.append("Necromancer")
                    necromancer_added = True  # Show that a necromanser has been added

    def place_heroes(self) -> None:
        mid = self.__width // 2  # Calculate middle

        if self.__width % 2 == 0:  #Even
            #Penultimate row
            self.__board[self.__height - 2][mid - 1] = self.__heroes[0]  #Warrior
            self.__board[self.__height - 2][mid] = self.__heroes[2]  #Paladin
            #Last row
            self.__board[self.__height - 1][mid - 1] = self.__heroes[1]  #Mage
            self.__board[self.__height - 1][mid] = self.__heroes[3]  #Ranger
        else:  #Odd
            #Penultimate row
            self.__board[self.__height - 2][mid] = self.__heroes[0]  #Warrior
            #Last row
            self.__board[self.__height - 1][mid - 1] = self.__heroes[1]  #Mage
            self.__board[self.__height - 1][mid] = self.__heroes[2]  #Paladin
            self.__board[self.__height - 1][mid + 1] = self.__heroes[3]  #Ranger

    def place_villains(self) -> None:
        for villain in self.__villains:
            placed = False
            while not placed:
                # Randomize a row
                row = random.randint(0, self.__height - 3)
                # Randomize a column
                col = random.randint(0, self.__width - 1)

                # Check if empty
                if self.__board[row][col] is None:
                    # Place the villain
                    self.__board[row][col] = villain
                    placed = True

    def generate_new_board(self, height: int = -1, width: int = -1) -> None:
        # Randomize height and width
        if height == -1 or width == -1:
            height = random.randint(4, 12)
            width = random.randint(4, 12)

        # Set height and width
        self.height = height
        self.width = width

        # Reset the board
        self.__board = [[None for i in range(self.__width)] for i in range(self.__height)]

        # Generate new villains
        self.generate_villains()

        # Place heroes
        self.place_heroes()

        # Place villains
        self.place_villains()
