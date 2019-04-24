# EE551_Python Project
# Author: Qiuyang Tang
# cite: "www.pygame.org"

import sys
import pygame
import random
import time
from settings import *

from gamedisplay import GameDisplay
from gamestate import GameState
from gameresource import GameResource


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Qiuyang's Tetris")
    pygame.key.set_repeat(HOLD_DELAY,
                          HOLD_MOVING_SPEED)  # hold key will keep creating same event, set_repeat(delay, interval)
    # background color
    bg_color = BG_COLOR
    # generate random block
    random.seed(int(time.time()))
    # wall = Wall(screen)
    # block = Block(random.choice(BLOCK_TYPES), screen, wall)
    game_state = GameState(screen)
    game_resource = GameResource()

    while True:
        # if touch bottom
        if game_state.block and game_state.block.touch_bottom:
            game_state.bottom()
        # if game_state.block.touch_bottom:
        #     game_state.wall.add_to_wall(game_state.block)
        #     game_state.add_score(game_state.wall.eliminate_line())
        #     game_state.block = Block(random.choice(BLOCK_TYPES), screen, game_state.wall)

        # monitor keyboard and mouse event
        check_events(game_state)

        # fill background
        screen.fill(bg_color)
        # draw one cell
        if game_state.block:
            game_state.block.paint()
        # draw game area and wall
        GameDisplay.draw_game_area(screen, game_state)

        # refresh the screen
        pygame.display.flip()


# keyboard and mouse event
def check_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            press_key_down(event, game_state)
        elif event.type == pygame.USEREVENT:
            game_state.block.move_down()


def press_key_down(event, game_state):
    if not game_state.paused and event.key == pygame.K_DOWN:
        if game_state.block:
            game_state.block.move_down()
    elif not game_state.paused and event.key == pygame.K_UP:
        if game_state.block:
            game_state.block.turn()
    elif not game_state.paused and event.key == pygame.K_RIGHT:
        if game_state.block:
            game_state.block.move_right()
    elif not game_state.paused and event.key == pygame.K_LEFT:
        if game_state.block:
            game_state.block.move_left()
    elif not game_state.paused and event.key == pygame.K_SPACE:
        if game_state.block:
            game_state.block.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()


if __name__ == '__main__':
    main()
