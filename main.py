import pygame
import sys
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add Player class to both groups
    Player.containers = (updatable, drawable)

    # create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #start game loop
    game_loop(screen, clock, updatable, drawable)

def game_loop(screen, clock, updatable, drawable):
    dt = 0
    #check for game exit event
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # check for key presses
        for _ in updatable:
            _.update(dt)
        # redraw the screen and player
        screen.fill((0, 0, 0))
        
        for _ in drawable:
            _.draw(screen)
        # update the display
        pygame.display.flip()
        # update the delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()