'''
    no imports required for person class
'''
class Person():
    '''
        Person class acts as a general class having x and y co-ordinates
        which can move and have some other properties
    '''
    def __init__(self, kind, lefttop_x, lefttop_y):
        self.type = kind
        self._lefttop_x = lefttop_x
        self._lefttop_y = lefttop_y

    def get_lefttop_x(self):
        '''
            Indicates the top left x-coordinate
        '''
        return self._lefttop_x

    def get_lefttop_y(self):
        '''
            Indicates the top left y-coordinate
        '''
        return self._lefttop_y

    def get_persontype(self):
        '''
            Returns the type of person
        '''
        return self.type

    def set_lefttop_x(self, val):
        '''
            To set the top left x-coordinate.
        '''
        self._lefttop_x = val

    def set_lefttop_y(self, val):
        '''
            To set the top left y-coordinate.
        '''
        self._lefttop_y = val

    def populate_grid_with_person(self, grid):
        '''
            To create a person based on type on the board.
        '''
        if self.type == 1:
            x_var = self.get_lefttop_x()
            y_var = self.get_lefttop_y()
            grid[x_var][y_var] = 'B'
            grid[x_var][y_var + 1] = 'B'
            grid[x_var][y_var + 2] = 'B'
            grid[x_var][y_var + 3] = 'B'
            grid[x_var + 1][y_var] = 'B'
            grid[x_var + 1][y_var + 1] = 'B'
            grid[x_var + 1][y_var + 2] = 'B'
            grid[x_var + 1][y_var + 3] = 'B'
        elif self.type == 2:
            x_var = self.get_lefttop_x()
            y_var = self.get_lefttop_y()
            grid[x_var][y_var] = 'E'
            grid[x_var][y_var + 1] = 'E'
            grid[x_var][y_var + 2] = 'E'
            grid[x_var][y_var + 3] = 'E'
            grid[x_var + 1][y_var] = 'E'
            grid[x_var + 1][y_var + 1] = 'E'
            grid[x_var + 1][y_var + 2] = 'E'
            grid[x_var + 1][y_var + 3] = 'E'
        return grid

    def clear_grid_of_person(self, grid, move_type, detonation=0):
        '''
            To remove the person from the board
        '''
        if move_type == 0 or move_type == 3:
            x_var = self.get_lefttop_x()
            y_var = self.get_lefttop_y()
            grid[x_var][y_var] = ' '
            grid[x_var][y_var + 1] = ' '
            grid[x_var][y_var + 2] = ' '
            grid[x_var][y_var + 3] = ' '
            grid[x_var + 1][y_var] = ' '
            grid[x_var + 1][y_var + 1] = ' '
            grid[x_var + 1][y_var + 2] = ' '
            grid[x_var + 1][y_var + 3] = ' '
        if move_type == 1:
            x_var = self.get_lefttop_x()
            y_var = self.get_lefttop_y()
            grid[x_var][y_var] = str(detonation)
            grid[x_var][y_var + 1] = str(detonation)
            grid[x_var][y_var + 2] = str(detonation)
            grid[x_var][y_var + 3] = str(detonation)
            grid[x_var + 1][y_var] = str(detonation)
            grid[x_var + 1][y_var + 1] = str(detonation)
            grid[x_var + 1][y_var + 2] = str(detonation)
            grid[x_var + 1][y_var + 3] = str(detonation)
        return grid

    def move(self, direction, grid, move_type, detonation):
        '''
            Move function takes care of moving the person and clear the grid
            and keep tracking of the number of enemies and if bomberman dies
        '''
        if direction == 'a':
            if ((self.type == 1 and grid[self.get_lefttop_x()][self.get_lefttop_y() - 3] == 'E')
                    and (grid[self.get_lefttop_x() + 1][self.get_lefttop_y() - 3] == 'E')):
                grid = self.bomber_man_suicide(grid, move_type)
            elif grid[self.get_lefttop_x()][self.get_lefttop_y() - 1] == ' ' or move_type == 3:
                grid = self.clear_grid_of_person(grid, move_type, detonation)
                self.set_lefttop_x(self.get_lefttop_x())
                self.set_lefttop_y(self.get_lefttop_y() - 4)
                grid = self.populate_grid_with_person(grid)
        if direction == 'd':
            if ((self.type == 1) and (grid[self.get_lefttop_x()][self.get_lefttop_y() + 5] == 'E')
                    and (grid[self.get_lefttop_x() + 1][self.get_lefttop_y() + 5] == 'E')):
                grid = self.bomber_man_suicide(grid, move_type)
            elif grid[self.get_lefttop_x()][self.get_lefttop_y() + 4] == ' ' or move_type == 3:
                grid = self.clear_grid_of_person(grid, move_type, detonation)
                self.set_lefttop_x(self.get_lefttop_x())
                self.set_lefttop_y(self.get_lefttop_y() + 4)
                grid = self.populate_grid_with_person(grid)
        if direction == 'w':
            if (self.type == 1 and grid[self.get_lefttop_x() - 2][self.get_lefttop_y() + 1] == 'E'
                    and (grid[self.get_lefttop_x() - 1][self.get_lefttop_y() + 1] == 'E')):
                grid = self.bomber_man_suicide(grid, move_type)
            elif grid[self.get_lefttop_x() - 1][self.get_lefttop_y()] == ' ' or move_type == 3:
                grid = self.clear_grid_of_person(grid, move_type, detonation)
                self.set_lefttop_x(self.get_lefttop_x() - 2)
                self.set_lefttop_y(self.get_lefttop_y())
                grid = self.populate_grid_with_person(grid)
        if direction == 's':
            if (self.type == 1 and grid[self.get_lefttop_x() + 2][self.get_lefttop_y() + 1] == 'E'
                    and (grid[self.get_lefttop_x() + 3][self.get_lefttop_y() + 1] == 'E')):
                grid = self.bomber_man_suicide(grid, move_type)
            elif grid[self.get_lefttop_x() + 2][self.get_lefttop_y()] == ' ' or move_type == 3:
                grid = self.clear_grid_of_person(grid, move_type, detonation)
                self.set_lefttop_x(self.get_lefttop_x() + 2)
                self.set_lefttop_y(self.get_lefttop_y())
                grid = self.populate_grid_with_person(grid)
        return grid
    @classmethod
    def check_if_bomberman(cls, grid, lefttop_x, lefttop_y):
        '''
            Returns True if it is Bomberman else false
        '''
        x_var = lefttop_x
        y_var = lefttop_y
        return grid[x_var][y_var] == 'B'

    def bomber_man_suicide(self, grid, move_type):
        '''
            this function is used when bomberman commits suicide by
            getting himself killed because of the bomb.
        '''
        grid = self.clear_grid_of_person(grid, move_type)
        return [grid, 0]
