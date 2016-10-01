import sys, pygame

pygame.init()
screen = pygame.display.set_mode((320,240))
pygame.Surface.fill(screen, (0,0,0))

fly = pygame.sprite.Sprite()
fly.image = pygame.image.load("test.bmp") #this is a surface
fly.rect = fly.image.get_rect()

#add to a group
fg = pygame.sprite.LayeredUpdates()
fg.add( fly )

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    fg.draw( screen )
    pygame.display.flip()
        
        
    
