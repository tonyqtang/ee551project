SCREEN_WIDTH = 600
SCREEN_HEIGHT = 750
CELL_WIDTH = 28  # each cell size (pixels)
COLUMN_NUM = 12
LINE_NUM = 24
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM  # 10 cells one row
GAME_AREA_HEIGHT = CELL_WIDTH * LINE_NUM  # 20 rows
GAME_AREA_LEFT = CELL_WIDTH * 2  # width of left blank area
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT - 40  # width of top blank area

EDGE_COLOR = (0, 0, 0)  # black
CELL_COLOR = (100, 100, 100)
BG_COLOR = (0, 0, 0)

HOLD_DELAY = 150
HOLD_MOVING_SPEED = 40

# shapes of blocks
S_SHAPE_TEMPLATE = [['0110',
                     '1100',
                     '0000'],
                    ['0100',
                     '0110',
                     '0010']]

Z_SHAPE_TEMPLATE = [['1100',
                     '0110',
                     '0000'],
                    ['0010',
                     '0110',
                     '0100']]
I_SHAPE_TEMPLATE = [['0100',
                     '0100',
                     '0100',
                     '0100'],
                    ['0000',
                     '1111',
                     '0000',
                     '0000']]
O_SHAPE_TEMPLATE = [['11',
                     '11']]
J_SHAPE_TEMPLATE = [['010',
                     '010',
                     '110'],
                    ['100',
                     '111',
                     '000'],
                    ['011',
                     '010',
                     '010'],
                    ['000',
                     '111',
                     '001']]
L_SHAPE_TEMPLATE = [['100',
                     '100',
                     '110'],
                    ['000',
                     '111',
                     '100'],
                    ['110',
                     '010',
                     '010'],
                    ['001',
                     '111',
                     '000']]
T_SHAPE_TEMPLATE = [['000',
                     '111',
                     '010'],
                    ['010',
                     '110',
                     '010'],
                    ['010',
                     '111',
                     '000'],
                    ['010',
                     '011',
                     '010']]

BLOCK = {'S': S_SHAPE_TEMPLATE,
         'Z': Z_SHAPE_TEMPLATE,
         'I': I_SHAPE_TEMPLATE,
         'O': O_SHAPE_TEMPLATE,
         'J': J_SHAPE_TEMPLATE,
         'L': L_SHAPE_TEMPLATE,
         'T': T_SHAPE_TEMPLATE}

BLOCK_TYPES = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']

BLOCK_COLOR = {'S': (0, 255, 128),  # green
               'Z': (255, 128, 255),  # rose red
               'I': (128, 0, 255),  # violet
               'O': (0, 0, 255),  # blue
               'J': (0, 128, 0),  # dark green
               'L': (255, 0, 0),  # red
               'T': (255, 128, 0)  # orange
               }
CUBE_COLORS = [
    (0xcc, 0x99, 0x99), (0xff, 0xff, 0x99), (0x66, 0x66, 0x99),
    (0x99, 0x00, 0x66), (0xff, 0xcc, 0x00), (0xcc, 0x00, 0x33),
    (0xff, 0x00, 0x33), (0x00, 0x66, 0x99), (0xff, 0xff, 0x33),
    (0x99, 0x00, 0x33), (0xcc, 0xff, 0x66), (0xff, 0x99, 0x00)
]

WALL_BLANK_LABEL = '-'

TIMER_INTERVAL = 1000  # auto-falling speed

SCORE_FONT = 'bitstreamverasans'
SCORE_SIZE = 33
SCORE_COLOR = (255, 0, 0)

EDGE_WIDTH = 3
MARGIN_WIDTH = 25

DIFFICULTY_LEVEL_INTERVAL = 100
TIMER_FASTER_VALUE = 50

WHITE = (255, 255, 255)
GRID_COLOR = (51, 51, 51)
