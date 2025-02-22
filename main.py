import sys
import pygame
from asteroid import Asteroid
from asteroidField import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    # Set up containers for both classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)  # Add this with your other container assignments

    # Then create instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #SETS THE COLOR OF THE WINDOW
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for a in asteroids:
            if a.collision(player):
                print("Game Over")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


    
if __name__ == "__main__":
    main()