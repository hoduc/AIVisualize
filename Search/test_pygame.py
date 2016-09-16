import sys, pygame

pygame.init()

size = width, height = 320, 320
BLOCK_SIZE = 32
black = 0, 0 ,0
red = 255, 0, 0
green = 0, 255, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
start = 0,0
goal = width/BLOCK_SIZE, height/BLOCK_SIZE

pygame.Surface.fill(screen, black)
pygame.draw.circle( screen, red, (10, 20 ), 5)
pygame.draw.circle( screen, green, (15, 30), 5 )
#pygame.draw.circle( screen, red, (start[0] + BLOCK_SIZE/2, start[1] + BLOCK_SIZE/2), BLOCK_SIZE/2 )
#pygame.draw.circle( screen, green, ((start[0]+BLOCK_SIZE)*(BLOCK_SIZE-1), (start[1]+BLOCK_SIZE)*(BLOCK_SIZE-1)), BLOCK_SIZE/2 )
#pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip()
