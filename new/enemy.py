'''
    enemy inherits the person class and random is used for a random move
'''

import random
from person import Person


class Enemy(Person):
    '''
        The enemy inherits the person class and has a function random move
        used to move the enemy randomly on the board
    '''
    def __init__(self, lefttop_x, lefttop_y, kind):
        Person.__init__(self, kind, lefttop_x, lefttop_y)

    def random_move(self, grid):
        '''
            The RandomMove function takes a the topmost x,y coordinates of The
            enemy and checks all the grids and takes the possible positions
            into an array and selects a random move
        '''
        x_var = self.get_lefttop_x()
        y_var = self.get_lefttop_y()
        possible_pos = []

        if ((grid[x_var][y_var - 1] == ' ' or self.check_if_bomberman(grid, x_var, y_var - 1))
                and (x_var != 2 or y_var != 8)):
            possible_pos.append('a')

        if grid[x_var][y_var + 4] == ' ' or self.check_if_bomberman(grid, x_var, y_var + 4):
            possible_pos.append('d')

        if ((grid[x_var - 1][y_var] == ' ' or self.check_if_bomberman(grid, x_var - 1, y_var))
                and (x_var != 4 or y_var != 4)):
            possible_pos.append('w')

        if grid[x_var + 2][y_var] == ' ' or self.check_if_bomberman(grid, x_var + 2, y_var):
            possible_pos.append('s')

        if possible_pos == []:
            return 'no move'
        move_pos = random.choice(possible_pos)
        if move_pos == 'a' and self.check_if_bomberman(grid, x_var, y_var - 4):
            return [move_pos, 3]

        if move_pos == 'd' and self.check_if_bomberman(grid, x_var, y_var + 4):
            return [move_pos, 3]

        if move_pos == 'w' and self.check_if_bomberman(grid, x_var - 2, y_var):
            return [move_pos, 3]

        if move_pos == 's' and self.check_if_bomberman(grid, x_var + 2, y_var):
            return [move_pos, 3]

        return [move_pos, 0]
