import pygame
import sys
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop(screen, clock, player)

def game_loop(screen, clock, player):
    dt = 0
    #check for game exit event
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # check for key presses
        player.update(dt)
        # redraw the screen and player
        screen.fill((0, 0, 0))
        player.draw(screen)
        # update the display
        pygame.display.flip()
        # update the delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()