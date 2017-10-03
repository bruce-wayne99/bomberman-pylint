'''
    It works same as the Bricks class and returns a 2-D array
    of the corresponding length and width given
'''

class Walls():
    '''
        The wall class has attributes length and width of the wall
        and builds a 2-D array of corresponding length and width
        and stores in an attribute named 'wall'.
    '''
    def __init__(self, length, width):
        self.length = length
        self.width = width
        wall = [['X' for _ in range(length)] for _ in range(width)]
        self.wall = wall

    def get_wall(self):
        '''
            Returns the 2-D array of the wall.
        '''
        return self.wall

    def wall_length(self):
        '''
            Returns the length of the wall.
        '''
        return self.length

    def wall_width(self):
        '''
            Returns the width of the wall.
        '''
        return self.width
