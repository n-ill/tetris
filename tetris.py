import pygame

WIDTH = 310
HEIGHT = 620

#setup
pygame.init()
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

def create_grid():
    grid = []
    for x in range(10):
        for y in range(20):
            grid.append(pygame.Rect((30*x)+x,(30*y)+y,30,30))

    return grid


class l_piece():

    def __init__(self):
        self.color = (0,255,255) #cyan
        self.blocks = [pygame.Rect((30*i)+i,0,30,30)  for i in range(4)] #initally horizontal

    def rotate(self):
        self.blocks = [pygame.Rect(0,(30*i)+i,30,30)  for i in range(4)] #vertical



game_speed = 5
count = 0
running = True
#main game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_display.fill(pygame.Color(50, 50, 50))

    grid = create_grid()
    for rect in grid:
        pygame.draw.rect(game_display, pygame.Color('black'), rect)

    piece1 = l_piece()
    for block in piece1.blocks:
        if count < HEIGHT - 30:
            block.move(0,count)
        pygame.draw.rect(game_display, piece1.color, block)

    count += 1

    pygame.display.flip()
    clock.tick(60)