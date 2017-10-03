''' Brick class takes the length and width of the brick and
    outputs the a brick of the corresponding dimensions in
    a 2-D array
'''

class Bricks():
    '''
        The wall class has attributes length and width of the wall
        and builds a 2-D array of corresponding length and width
        and stores in an attribute named 'wall'.
    '''
    def __init__(self, length, width):
        self.length = length
        self.width = width
        brick = [['/' for _ in range(length)] for _ in range(width)]
        self.brick = brick

    def get_brick(self):
        '''
            Returns the 2-D array of the brick.
        '''
        return self.brick

    def wall_length(self):
        '''
            Returns the length of the brick.
        '''
        return self.length

    def wall_width(self):
        '''
            Returns the width of the brick.
        '''
        return self.width
