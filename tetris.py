import pygame

def create_grid(): # 2d list of Rect objects
    grid = []
    for x in range(10):
        col = []
        for y in range(20):
            col.append(pygame.Rect((30*x)+x,(30*y)+y,30,30))
        grid.append(col)
    return grid

grid = create_grid() # 10x20 game grid

class Piece:

    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.rotation = 0

    def rotate(self):
        if self.rotation < 3:
            self.rotation += 1
        else:
            self.rotation = 0

    def move_left(self):
        self.x_pos -= 1

    def move_right(self):
        self.x_pos += 1

class L_Piece(Piece):

    def __init__(self, x, y):
        self.color = (0,255,255) #cyan
        super().__init__(x, y)

    def draw(self):
        if self.rotation == 0 or self.rotation == 2:
            for i in range(4):
                pygame.draw.rect(game_display, curr_piece.color, grid[curr_piece.x_pos + i][curr_piece.y_pos])
        else:
            for i in range(4):
                pygame.draw.rect(game_display, curr_piece.color, grid[curr_piece.x_pos][curr_piece.y_pos + i])


def draw_grid(a_2d_list):
    for list in a_2d_list:
        for rect in list:
            pygame.draw.rect(game_display, pygame.Color('black'), rect)


WIDTH = 310
HEIGHT = 620

#setup
pygame.init()
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()


curr_piece = L_Piece(4,0)
count = 15
running = True
#main game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_display.fill(pygame.Color(50, 50, 50))

    draw_grid(grid)
    curr_piece.draw()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and curr_piece.x_pos > 0:
        curr_piece.move_left()
    if keys[pygame.K_RIGHT] and curr_piece.x_pos < 6:
        curr_piece.move_right()
    if keys[pygame.K_UP]:
        curr_piece.rotate()

    if curr_piece.y_pos < 19 and count == 15:
        curr_piece.y_pos += 1
        count = 0

    count += 1
    pygame.display.flip()
    clock.tick(15)