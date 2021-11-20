
import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

player_surf = pygame.image.load('player_walk_1.png')
player_rect = player_surf.get_rect(topleft = (0,0))

while True:
    for event in pygame.event.get():#
        if event.type == pygame.QUIT:
            pygame.exit()
            exit()

    screen.blit(player_surf,player_rect)

    pygame.display.update()  # Update the display
    clock.tick(60)
