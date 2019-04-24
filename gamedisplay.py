from settings import *
import pygame


class GameDisplay:
    # @staticmethod
    # def draw_cell(screen, row, column, color):
    #     '''fill #row #column with color'''
    #     cell_position = (column * CELL_WIDTH + GAME_AREA_LEFT + 1,
    #                      row * CELL_WIDTH + GAME_AREA_TOP + 1)
    #     cell_inner = pygame.Rect(cell_position, (CELL_WIDTH - 2, CELL_WIDTH - 2))
    #     cell_outer = pygame.Rect(cell_position, (CELL_WIDTH, CELL_WIDTH))
    #     pygame.draw.rect(screen, color, cell_inner)
    #     pygame.draw.rect(screen, WHITE, cell_outer, 2)

    @staticmethod
    def draw_cell(screen, cell_position, color):

        # left_top_anchor = (left_top_anchor[0] + 1, left_top_anchor[1] + 1)
        # cell_size = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_inner = pygame.Rect(cell_position, (CELL_WIDTH - 2, CELL_WIDTH - 2))
        cell_outer = pygame.Rect(cell_position, (CELL_WIDTH, CELL_WIDTH))
        pygame.draw.rect(screen, color, cell_inner)
        pygame.draw.rect(screen, WHITE, cell_outer, 2)
        # cell_rect = pygame.Rect(left_top_anchor, cell_size)
        # pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_game_area(screen, game_state):
        # for r in range(LINE_NUM + 1):
        #     pygame.draw.line(screen, GRID_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
        #                      (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
        #
        # for c in range(COLUMN_NUM + 1):
        #     pygame.draw.line(screen, GRID_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
        #                      (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))
        GameDisplay.draw_border(screen, GAME_AREA_LEFT, GAME_AREA_TOP, LINE_NUM, COLUMN_NUM)
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen, game_state.game_score)
        # if game_state.stopped:
        #     if game_state.session_count > 0:
        #         GameDisplay.draw_game_over(screen, game_resource)
        #     GameDisplay.draw_start(screen, game_resource)
        # if game_state.paused:
        #     GameDisplay.draw_pause(screen, game_resource)
        GameDisplay.draw_next_block(screen, game_state.next_block)
        GameDisplay.draw_level(screen, game_state.level)
        GameDisplay.draw_mannual(screen)

    @staticmethod
    def draw_wall(game_wall):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, (c * CELL_WIDTH + GAME_AREA_LEFT + 1,
                                                             r * CELL_WIDTH + GAME_AREA_TOP + 1),
                                          BLOCK_COLOR[game_wall.area[r][c]])

    @staticmethod
    def draw_next_block(screen, next_block):
        start_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH * 2
        start_y = GAME_AREA_TOP
        # GameDisplay.draw_border(screen, start_x, start_y, 4, 4)

        if next_block:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            cells = []
            shape_template = BLOCK[next_block.shape]
            shape_turn = shape_template[next_block.dir]
            for r in range(len(shape_turn)):
                for c in range(len(shape_turn[0])):
                    if shape_turn[r][c] == "1":
                        cells.append((c, r, BLOCK_COLOR[next_block.shape]))

            max_c = max([cell[0] for cell in cells])
            min_c = min([cell[0] for cell in cells])
            start_x += round((4 - (max_c - min_c + 1)) / 2 * CELL_WIDTH)
            max_r = max([cell[1] for cell in cells])
            min_r = min([cell[1] for cell in cells])
            start_y += round((4 - (max_r - min_r + 1)) / 2 * CELL_WIDTH)

            for cell in cells:
                color = cell[2]
                left_top = (
                start_x + (cell[0] - min_c) * CELL_WIDTH, start_y + (cell[1] - min_r) * CELL_WIDTH + GAME_AREA_TOP)
                GameDisplay.draw_cell(screen, left_top, color)

    # def show_text(screen, text, size, x, y, color=WHITE, bgColor=None):
    #     fontObj = pygame.font.SysFont('arial', size)
    #     textSurfaceObj = fontObj.render(text, True, color, bgColor)
    #     textRectObj = textSurfaceObj.get_rect()
    #     textRectObj.center = (x, y)
    #     screen.blit(textSurfaceObj, textRectObj)

    @staticmethod
    def draw_score(screen, score):
        scoreboard_font = pygame.font.SysFont('arial', 28)
        scoreboard_surface = scoreboard_font.render('Score : {}'.format(score), True, WHITE)
        scoreboard_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 7 * CELL_WIDTH)
        screen.blit(scoreboard_surface, scoreboard_position)

        # score_font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)
        # score_surface = score_font.render(str(score), False, SCORE_COLOR)
        # scoreboard_width = scoreboard_surface.get_width()
        # score_position = (scoreboard_position[0] + scoreboard_width + 10, scoreboard_position[1])
        # screen.blit(score_surface, score_position)

    @staticmethod
    def draw_level(screen, level):
        level_label_font = pygame.font.SysFont('arial', 28)
        level_label_surface = level_label_font.render('Level : {}'.format(level), True, WHITE)
        level_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 9 * CELL_WIDTH)
        screen.blit(level_label_surface, level_label_position)

        # level_font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)
        # level_surface = level_font.render(str(level), False, SCORE_COLOR)
        # level_label_width = level_label_surface.get_width()
        # level_position = (level_label_position[0] + level_label_width + 10, level_label_position[1])
        # screen.blit(level_surface, level_position)

    @staticmethod
    def draw_start(screen, game_resource):
        start_tip_position = (GAME_AREA_LEFT + 2 * CELL_WIDTH, GAME_AREA_TOP + 10 * CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(), start_tip_position)

    @staticmethod
    def draw_pause(screen, game_resource):
        pause_position = (GAME_AREA_LEFT + 1 * CELL_WIDTH, GAME_AREA_TOP + 9 * CELL_WIDTH)
        screen.blit(game_resource.load_pausing_img(), pause_position)

        resume_tip_position = (GAME_AREA_LEFT + 1 * CELL_WIDTH, GAME_AREA_TOP + 11 * CELL_WIDTH)
        screen.blit(game_resource.load_continue_img(), resume_tip_position)

    @staticmethod
    def draw_game_over(screen, game_resource):
        gameover_position = (GAME_AREA_LEFT + 4 * CELL_WIDTH - CELL_WIDTH // 2, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_gameover_img(), gameover_position)

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        points = [(start_x - EDGE_WIDTH, start_y - EDGE_WIDTH),
                  (start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y - EDGE_WIDTH),
                  (start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y + EDGE_WIDTH + line_num * CELL_WIDTH),
                  (start_x - EDGE_WIDTH, start_y + EDGE_WIDTH + line_num * CELL_WIDTH)
                  ]
        pygame.draw.lines(screen, WHITE, 1, points, 3)

        # top_border = pygame.Rect(start_x, start_y,  EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        # pygame.draw.rect(screen, EDGE_COLOR, top_border)
        #
        # left_border = pygame.Rect(start_x, start_y, EDGE_WIDTH, EDGE_WIDTH + line_num * CELL_WIDTH)
        # pygame.draw.rect(screen, EDGE_COLOR, left_border)
        #
        # right_border = pygame.Rect(start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y, EDGE_WIDTH,
        #                            EDGE_WIDTH + line_num * CELL_WIDTH)
        # pygame.draw.rect(screen, EDGE_COLOR, right_border)
        #
        # bottom_border = pygame.Rect(start_x, start_y + EDGE_WIDTH + line_num * CELL_WIDTH,
        #                              EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        # pygame.draw.rect(screen, EDGE_COLOR, bottom_border)

    @staticmethod
    def draw_mannual(screen):
        a = pygame.font.SysFont('arial', 24)
        b = a.render('START : S', True, WHITE)
        position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 19 * CELL_WIDTH)
        screen.blit(b, position)

        a = pygame.font.SysFont('arial', 24)
        b = a.render(u'CONTROL : ← →', True, WHITE)
        position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 20 * CELL_WIDTH)
        screen.blit(b, position)

        a = pygame.font.SysFont('arial', 24)
        b = a.render(u'CHANGE DIR : ↑', True, WHITE)
        position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 21 * CELL_WIDTH)
        screen.blit(b, position)

        a = pygame.font.SysFont('arial', 24)
        b = a.render('FALL : SPACE', True, WHITE)
        position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 22 * CELL_WIDTH)
        screen.blit(b, position)

        a = pygame.font.SysFont('arial', 24)
        b = a.render('PAUSE : P ', True, WHITE)
        position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 23 * CELL_WIDTH)
        screen.blit(b, position)
