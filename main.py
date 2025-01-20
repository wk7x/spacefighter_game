import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot
from powercounter import PowerUpCounter
from scorecounter import ScoreCounter

def main():
    # initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    highscore = 0
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
    PowerUpCounter.containers = (updatable, drawable)
    ScoreCounter.containers = (updatable, drawable)
    
    # create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # create the score counter
    score_counter = ScoreCounter()

    # create the power up counter
    power_up_counter = PowerUpCounter()

    # Asteroid movement
    asteroid_field = AsteroidField()
    
    #   start game loop
    display_start_menu(screen, score_counter, power_up_counter, clock, player, updatable, drawable, asteroids, shots)   

def display_start_menu(screen, score_counter, power_up_counter, clock, player, updatable, drawable, asteroids, shots):
    font = pygame.font.Font(None, 36)
    line1 = "Welcome! Press [Enter] to start or [Esc] to exit."
    line2 = "Controls: [W] Up, [S] Down, [A] Left, [D] Right, [Space] Shoot, [E] Mega-Blast (Recharges every 15 seconds)"
    
    # Calculate y positions
    y1 = SCREEN_HEIGHT / 2 - 40  # Adjust as needed for spacing
    y2 = SCREEN_HEIGHT / 2

    text1 = font.render(line1, True, (57, 255, 20))  # Neon green
    text_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, y1))
    screen.blit(text1, text_rect1)

    text2 = font.render(line2, True, (128, 0, 128))  # Purple
    text_rect2 = text2.get_rect(center=(SCREEN_WIDTH / 2, y2))
    screen.blit(text2, text_rect2)

    pygame.display.flip()

    # Event handling
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop(screen, score_counter, power_up_counter, clock, player, updatable, drawable, asteroids, shots)
                    return  # Exit the menu and start the game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    

def game_loop(screen, score_counter, power_up_counter, clock, player, updatable, drawable, asteroids, shots):
    dt = 0

    #check for game exit event
    while True:
 
        power_up_counter.recharge()
        
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
                
                while True:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Game over! Press [Enter] to try again or [Esc] to exit", True, (255, 255, 255))
                    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                    screen.blit(text, text_rect)
                    # Update display
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                main()
                                return
                            elif event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit()
        
        # check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_detector(asteroid):
                    rubble = asteroid.split()
                    shot.kill()
                    if rubble is None:
                        score_counter.addscore()

        # redraw the screen
        screen.fill((0, 0, 0))
        # draw the drawable objects
        for _ in drawable:
            _.draw(screen)

        power_up_counter.render(screen)
        score_counter.render(screen)
        # update the display
        pygame.display.flip()
        # update the delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()