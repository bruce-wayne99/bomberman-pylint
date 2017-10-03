'''
    imports include random
    and walls bricks and colorama for the colors
'''
from random import random
from walls import Walls
from bricks import Bricks
from enemy import Enemy
from colorama import Fore


class Board(Walls, Bricks):
    '''
        Board inherits walls and bricks classes
    '''
    def __init__(self, rows, columns, brickslimit):
        self.rows = rows
        self.columns = columns
        self._brickslimit = brickslimit
        Walls.__init__(self, 2, 4)
        Bricks.__init__(self, 2, 4)
        self.enemies = []

    def getbrickslimit(self):
        '''
            Returns the limit of bricks
        '''
        return self._brickslimit

    def setbrickslimit(self, val):
        '''
            To set the bricklimits
        '''
        self._brickslimit = val

    def create_empty_board(self):
        '''
            Returns a empty board
        '''
        grid = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        return grid

    @classmethod
    def populate_board_with_element(cls, x_var, y_var, grid, temp):
        '''
            This function exhibits polymorphism for both brick and wall elements
        '''
        grid[x_var][y_var] = temp[0][0]
        grid[x_var][y_var + 1] = temp[0][1]
        grid[x_var][y_var + 2] = temp[0][2]
        grid[x_var][y_var + 3] = temp[0][3]
        grid[x_var + 1][y_var] = temp[1][0]
        grid[x_var + 1][y_var + 1] = temp[1][1]
        grid[x_var + 1][y_var + 2] = temp[1][2]
        grid[x_var + 1][y_var + 3] = temp[1][3]
        return grid

    def populate_board_with_walls(self, grid):
        '''
            Populates the board with walls at the required positions
        '''
        x_var = 0
        y_var = 0
        while y_var < self.columns:
            wall = Walls(4, 2)
            temp = wall.wall
            grid = self.populate_board_with_element(x_var, y_var, grid, temp)
            y_var += 4
        x_var = self.rows - 2
        y_var = 0
        while y_var < self.columns:
            wall = Walls(4, 2)
            temp = wall.wall
            grid = self.populate_board_with_element(x_var, y_var, grid, temp)
            y_var += 4
        x_var = 4
        y_var = 0
        while x_var < self.rows - 2:
            while y_var < self.columns:
                wall = Walls(4, 2)
                temp = wall.wall
                grid = self.populate_board_with_element(x_var, y_var, grid, temp)
                y_var += 8
            x_var += 4
            y_var = 0
        x_var = 0
        y_var = 0
        while x_var < self.rows:
            wall = Walls(4, 2)
            temp = wall.wall
            grid = self.populate_board_with_element(x_var, y_var, grid, temp)
            x_var += 2
        x_var = 0
        y_var = self.columns - 4
        while x_var < self.rows:
            wall = Walls(4, 2)
            temp = wall.wall
            grid = self.populate_board_with_element(x_var, y_var, grid, temp)
            x_var += 2
        return grid

    def brick_nested_condition(self, i, j, count):
        '''
            Checks the nested condition
        '''
        if (random() > 0.7 and count < self.getbrickslimit()
                and (i != 2 or j != 4)):
            if (i != 2 or j != 8) and (i != 4 or j != 4):
                return True
            return False
        return False
    @classmethod
    def enemies_nested_condition(cls, i, j, max_enemies, count):
        '''
            Checks the nested condition
        '''
        if (random() > 0.9 and count < max_enemies
                and (i != 2 or j != 4)):
            if (i != 2 or j != 8) and (i != 4 or j != 4):
                return True
            return False
        return False

    def populate_board_with_bricks(self, grid):
        '''
            Populates the board with bricks at random positions using random number
        '''
        count = 0
        for i in range(2, self.rows - 2):
            if i % 2 == 0:
                for j in range(4, self.columns - 4):
                    if j % 4 == 0 and grid[i][j] != 'X':
                        if self.brick_nested_condition(i, j, count):
                            brick = Bricks(4, 2)
                            temp = brick.brick
                            grid = self.populate_board_with_element(i, j, grid, temp)
                            count = count + 1
        return grid

    def populate_board_with_enemies(self, grid, max_enemies):
        '''
            Populates the board with enemies at random positions
        '''
        count = 0
        for i in range(2, self.rows - 2):
            if i % 2 == 0:
                for j in range(4, self.columns - 4):
                    if j % 4 == 0 and grid[i][j] == ' ':
                        if self.enemies_nested_condition(i, j, max_enemies, count):
                            enemy = Enemy(i, j, 2)
                            self.enemies.append(enemy)
                            grid = enemy.populate_grid_with_person(grid)
                            count = count + 1
        return grid

    def remove_enemy_from_list(self, x_var, y_var):
        '''
            Whenever an enemy dies he is removed from the
            enemies array based on his position
        '''
        for i in range(len(self.enemies)):
            if (self.enemies[i].get_lefttop_x() == x_var and
                    self.enemies[i].get_lefttop_y() == y_var):
                self.enemies.remove(self.enemies[i])
                break

    @classmethod
    def print_board(cls, grid):
        '''
            Function used to show that board printed with colored notion
        '''
        for i in grid:
            for j in i:
                if j == 'B':
                    print(Fore.CYAN + j, end="")
                elif j == 'X':
                    print(Fore.YELLOW + j, end="")
                elif j == '/':
                    print(Fore.MAGENTA + j, end="")
                elif j == 'E':
                    print(Fore.RED + j, end="")
                elif j == 'e':
                    print(Fore.GREEN + j, end="")
                else:
                    print(Fore.WHITE + j, end="")
            print("")
