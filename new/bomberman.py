'''
    modules written to import Person class and
    Bomb class from person.py and bomb.py respectively.
'''

from person import Person
from bomb import Bomb

class Bomberman(Person):
    '''
        Bomberman class used for defining a bomberman and
        inherits the person class.
    '''
    def __init__(self, lefttop_x, lefttop_y):
        Person.__init__(self, 1, lefttop_x, lefttop_y)
        self._det = 1
        self.active = []

    def set_detonation(self, val):
        '''
            To set the detonation
        '''
        self._det = val

    def get_detonation(self):
        '''
            To get the value of detonation
        '''
        return self._det

    def plot_bomb(self, grid, radius, timelimit, det):
        '''
            plot bomb function plots a new bomb and appends the bomb
            to active array of the bomberman attribute.
        '''
        new_bomb = Bomb([radius, timelimit, det], 3, self.get_lefttop_x(),
                        self.get_lefttop_y())
        self.active.append(new_bomb)
        return grid

    def bomber_man_suicide(self, grid, move_type):
        '''
            this function is used when bomberman commits suicide by
            getting himself killed because of the bomb.
        '''
        grid = self.clear_grid_of_person(grid, move_type)
        return [grid, 0]
