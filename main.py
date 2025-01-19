import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    # initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add Player class to both groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, shots, drawable)
    # create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #start game loop
    game_loop(screen, clock, player, updatable, drawable, asteroids, shots)

def game_loop(screen, clock, player, updatable, drawable, asteroids, shots):
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

        # check for collisions
        for asteroid in asteroids:
            if player.collision_detector(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        # check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_detector(asteroid):
                    asteroid.split()
                    shot.kill()

        # redraw the screen
        screen.fill((0, 0, 0))
        # draw the drawable objects
        for _ in drawable:
            _.draw(screen)
        # update the display
        pygame.display.flip()
        # update the delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()