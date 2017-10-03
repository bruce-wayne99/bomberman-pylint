'''
    imports for managing the input and for timeout
'''
import os
import sys
import signal
import time
import getch
from colorama import Fore

from board import Board
from bomberman import Bomberman


TIMEOUT = 1

def interrupted(_signum, _frame):
    '''
        interrupted is a function which is called if the input is not given
        within 1 second of time
    '''
    return 'interrupted'


signal.signal(signal.SIGALRM, interrupted)

def input_char():
    '''
        input_char is the function used to take the input which returns the character
        that is entered otherwise returns a zero(null)
    '''
    try:
        char = getch.getch()
        return char
    except BaseException:
        return 0

LEVEL = 1
MAX_LIFES = 2
TOTAL_SCORE = 0
MAX_ENEMIES = 6
BRICKSLIMIT = 40
BOX = []

while LEVEL <= 3:

    BOARD = Board(42, 84, BRICKSLIMIT)
    GRID = BOARD.create_empty_board()
    GRID = BOARD.populate_board_with_walls(GRID)
    GRID = BOARD.populate_board_with_bricks(GRID)
    MAN = Bomberman(2, 4)
    GRID = MAN.populate_grid_with_person(GRID)
    GRID = BOARD.populate_board_with_enemies(GRID, MAX_ENEMIES)
    ENEMIES = len(BOARD.enemies)
    COUNT = 0
    DETONATION = 0
    ACTIVE = 0
    MOVE_TYPE = 0
    SCORE = 0
    FLAG = 0
    RESETFLAG = 0
    NEXTINPUT = time.time() + 1
    '''
        This is a FLAG used to allow SYNCHRONOUS motion of the enemies and bomb
        DETONATION
    '''
    SYNCHRONOUS = 0
    TIMER = 200

    def reset_game(grid, man):
        '''
            To reset the game whenever the bomberman dies
        '''
        man = Bomberman(2, 4)
        grid = man.populate_grid_with_person(grid)
        return [grid, man]

    def check_to_end(max_lifes, enemies):
        '''
            To check if the no of lifes are finished for the bomberman
            to exit the game
        '''
        if max_lifes == -1:
            BOARD.print_board(GRID)
            print(Fore.WHITE + "GAME OVER")
            print(Fore.BLUE + "YOUR SCORE: ",
                  Fore.WHITE + str(TOTAL_SCORE + SCORE))
            sys.exit()
        if enemies == 0:
            return 1
        return 0

    while TIMER >= 0:
        signal.alarm(TIMEOUT)
        BOARD.print_board(GRID)
        print(Fore.RED + "LIFES AVAILABLE : ",
              Fore.WHITE + str(MAX_LIFES),
              '\t',
              Fore.MAGENTA + "YOUR SCORE : ",
              Fore.WHITE + str(TOTAL_SCORE + SCORE),
              '\t',
              Fore.GREEN + "TIME : ",
              Fore.WHITE + str(TIMER),
              '\t',
              Fore.CYAN + "Level :",
              Fore.WHITE + str(LEVEL))

        if ACTIVE == -1:
            ACTIVE = 0
            DETONATION = 0
            GRID = MAN.active[0].clear_grid_after_blast(GRID, BOX[3])
            MAN.active = []
            if FLAG == 1:
                MAX_LIFES -= 1
                check_to_end(MAX_LIFES, ENEMIES)
                MAN = Bomberman(2, 4)
                GRID = MAN.populate_grid_with_person(GRID)
                MOVE_TYPE = 0
                FLAG = 0
        if SYNCHRONOUS == 1:
            SYNCHRONOUS = 0
            NEXTINPUT = time.time() + 1
            if ACTIVE == 1:
                FLAG = 0
                DETONATION += 1
                BOX = MAN.active[0].check_if_time(
                    GRID, DETONATION, [ENEMIES, 1], SCORE)
                GRID = BOX[0]
                SCORE = BOX[5]
                if BOX[3] == []:
                    MAN.active[0].set_detonation(
                        MAN.active[0].get_detonation() - 1)
                    MAN.set_detonation(MAN.get_detonation() - 1)
                    if MOVE_TYPE != 1:
                        GRID = MAN.active[0].clear_grid_of_person(GRID, 1)
                if BOX[3]:
                    ACTIVE = -1
                    if BOX[2] == 0:
                        FLAG = 1
                    for num in BOX[4]:
                        BOARD.remove_enemy_from_list(num[0], num[1])
                        SCORE += 100
                        ENEMIES -= 1
            if check_to_end(MAX_LIFES, ENEMIES) == 1:
                break

        SYNCHRONOUS = 0
        RESETFLAG = 0
        INPUT_VALUE = input_char()
        if INPUT_VALUE == 'q':
            print(Fore.RED + "YOU QUIT THE GAME")
            print(Fore.WHITE + "GAME OVER")
            print(Fore.BLUE + "YOUR SCORE: ",
                  Fore.WHITE + str(TOTAL_SCORE + SCORE))
            sys.exit()
        if INPUT_VALUE != 0 and INPUT_VALUE != 'b':
            GRID = MAN.move(INPUT_VALUE, GRID, MOVE_TYPE, DETONATION)
            ESCAPED = 1
            if FLAG == 1:
                for ele in BOX[3]:
                    if ele[0] == MAN.get_lefttop_x(
                    ) and ele[1] == MAN.get_lefttop_y():
                        ESCAPED = 0
                        break
            if ESCAPED == 1:
                FLAG = 0
            if len(GRID) == 2:
                GRID = GRID[0]
                BOARD.print_board(GRID)
                print(Fore.RED +
                      "LIFES AVAILABLE : ", Fore.WHITE +
                      str(MAX_LIFES), '\t', Fore.MAGENTA +
                      "YOUR SCORE : ", Fore.WHITE +
                      str(TOTAL_SCORE +
                          SCORE), '\t', Fore.GREEN +
                      "TIME : ", Fore.WHITE +
                      str(TIMER), '\t', Fore.CYAN +
                      "Level :", Fore.WHITE +
                      str(LEVEL))
                MAX_LIFES -= 1
                RESETFLAG = 1
                check_to_end(MAX_LIFES, ENEMIES)
                if MAN.active != []:
                    GRID = MAN.active[0].clear_grid_of_person(GRID, 0)
                    if DETONATION == 3:
                        GRID = MAN.active[0].clear_grid_after_blast(GRID, BOX[3])
                TEMP = reset_game(GRID, MAN)
                GRID = TEMP[0]
                MAN = TEMP[1]
                FLAG = 0
                ACTIVE = 0
                DETONATION = 0
            MOVE_TYPE = 0
        if RESETFLAG == 1:
            continue

        if INPUT_VALUE == 'b':
            if MAN.active == []:
                GRID = MAN.plot_bomb(GRID, 1, 3, 2)
                MAN.set_detonation(2)
                MOVE_TYPE = 1
                ACTIVE = 1
                DETONATION = 0

        if time.time() >= NEXTINPUT:
            NEXTINPUT = time.time() + 1
            TIMER = TIMER - 1
            SYNCHRONOUS = 1
            RESETFLAG = 0
            for i in BOARD.enemies:
                RESETFLAG = 0
                TEMP = i.random_move(GRID)
                GRID = i.move(TEMP[0], GRID, TEMP[1], DETONATION)
                if TEMP[1] == 3:
                    BOARD.print_board(GRID)
                    print(Fore.RED +
                          "LIFES AVAILABLE : ", Fore.WHITE +
                          str(MAX_LIFES), '\t', Fore.MAGENTA +
                          "YOUR SCORE : ", Fore.WHITE +
                          str(TOTAL_SCORE +
                              SCORE), '\t', Fore.GREEN +
                          "TIME : ", Fore.WHITE +
                          str(TIMER), '\t', Fore.CYAN +
                          "LEVEL :", Fore.WHITE +
                          str(LEVEL))
                    MAX_LIFES -= 1
                    RESETFLAG = 1
                    if MAX_LIFES == -1:
                        print(Fore.WHITE + "GAME OVER")
                        print(Fore.BLUE + "YOUR SCORE: ",
                              Fore.WHITE + str(TOTAL_SCORE + SCORE))
                        sys.exit()
                    if MAN.active:
                        GRID = MAN.active[0].clear_grid_of_person(GRID, 0)
                        if DETONATION == 3:
                            GRID = MAN.active[0].clear_grid_after_blast(
                                GRID, BOX[3])
                    TEMP = reset_game(GRID, MAN)
                    GRID = TEMP[0]
                    MAN = TEMP[1]
                    FLAG = 0
                    ACTIVE = 0
                    MOVE_TYPE = 0
                    DETONATION = 0
                    break
            if RESETFLAG == 1:
                continue

        signal.alarm(0)
        os.system('clear')
    TOTAL_SCORE += SCORE
    LEVEL += 1
    MAX_LIFES += 1
    BRICKSLIMIT += 10
    MAX_ENEMIES += 3

    if TIMER == -1:
        print(Fore.WHITE + "GAME OVER")
        print(Fore.BLUE + "YOUR SCORE: ", Fore.WHITE + str(TOTAL_SCORE))
        sys.exit()

print(Fore.WHITE + "GAME OVER")
print(Fore.BLUE + "YOUR SCORE: ", Fore.WHITE + str(TOTAL_SCORE))
