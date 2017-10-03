'''
    Bomb class inherits the person class.
'''
from person import Person


class Bomb(Person):
    '''
        The class is used to declare a new bomb
    '''
    def __init__(self, bombattr, kind, lefttop_x, lefttop_y):
        Person.__init__(self, kind, lefttop_x, lefttop_y)
        self._radius = bombattr[0]            # Indicates the radius of the blast
        self._timelimit = bombattr[1]      # Indicates the detonation time
        self._det = bombattr[2]         # Used for displaying the counter on the bomb

    def get_timelimit(self):
        '''
            Returns the value of timelimit.
        '''
        return self._timelimit

    def set_timelimit(self, val):
        '''
            Returns the sets the value of timelimit.
        '''
        self._timelimit = val

    def set_detonation(self, val):
        '''
            To set the detonation of the bomb.
        '''
        self._det = val

    def get_detonation(self):
        '''
            To get the detonation of the bomb.
        '''
        return self._det

    def check_if_time(self, grid, detonation, personcount, score):
        '''
            check_if_time is used to check if the detonation time has occurred
            or not
        '''
        if detonation == self.get_timelimit():
            return self.explode(grid, personcount[0], personcount[1], score)
        return [grid, personcount[0], personcount[1], [], [], score]

    def explode(self, grid, enemycount, bombercount, score):
        '''
            If the detonation time has occurred it calls Explode which calls the
            which checks whether to collide with the grid or not and keeps track
            of all the enemies died in the process and also if the bomberman
            is dead
        '''
        x_var = self.get_lefttop_x()
        y_var = self.get_lefttop_y()
        box_var = self.collide([grid, x_var, y_var, enemycount, bombercount, 1], [],
                               [], score)
        box_var = self.collide([box_var[0], x_var, y_var + 4, box_var[1], box_var[2], 0]
                               , box_var[3], box_var[4], box_var[5])
        box_var = self.collide([box_var[0], x_var, y_var - 4, box_var[1], box_var[2], 0]
                               , box_var[3], box_var[4], box_var[5])
        box_var = self.collide([box_var[0], x_var + 2, y_var, box_var[1], box_var[2], 0]
                               , box_var[3], box_var[4], box_var[5])
        box_var = self.collide([box_var[0], x_var - 2, y_var, box_var[1], box_var[2], 0]
                               , box_var[3], box_var[4], box_var[5])
        return box_var

    def collide(self, obj, array, enemies_died, score):
        '''
            Appends the coordinates of enemies died to later
            remove from the enemy array
        '''
        if obj[0][obj[1]][obj[2]] != 'X':
            if obj[0][obj[1]][obj[2]] == '/':
                score += 20
            if obj[5] == 1 and self.check_if_bomberman(obj[0], obj[1], obj[2]):
                obj[4] -= 1
            if obj[0][obj[1]][obj[2]] == 'B' and obj[5] == 0:
                obj[4] -= 1
            if obj[0][obj[1]][obj[2]] == 'E' and obj[5] == 0:
                obj[3] -= 1

                enemies_died.append([obj[1], obj[2]])
            obj[0][obj[1]][obj[2]] = 'e'
            obj[0][obj[1]][obj[2] + 1] = 'e'
            obj[0][obj[1]][obj[2] + 2] = 'e'
            obj[0][obj[1]][obj[2] + 3] = 'e'
            obj[0][obj[1] + 1][obj[2]] = 'e'
            obj[0][obj[1] + 1][obj[2] + 1] = 'e'
            obj[0][obj[1] + 1][obj[2] + 2] = 'e'
            obj[0][obj[1] + 1][obj[2] + 3] = 'e'
            array.append([obj[1], obj[2]])  # Appends the positions to be cleared

        return [obj[0], obj[3], obj[4], array, enemies_died, score]
    @classmethod
    def clear_grid_after_blast(cls, grid, array):
        '''
            Used to clear the grid after the blast has occured
        '''
        for ele in array:
            grid[ele[0]][ele[1]] = ' '
            grid[ele[0]][ele[1] + 1] = ' '
            grid[ele[0]][ele[1] + 2] = ' '
            grid[ele[0]][ele[1] + 3] = ' '
            grid[ele[0] + 1][ele[1]] = ' '
            grid[ele[0] + 1][ele[1] + 1] = ' '
            grid[ele[0] + 1][ele[1] + 2] = ' '
            grid[ele[0] + 1][ele[1] + 3] = ' '
        return grid
