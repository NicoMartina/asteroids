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
    bullets = pygame.sprite.Group()

    # Set up containers for both classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, bullets)  # Add this with your other container assignments

    # Then create instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Debug prints
        print(f"Number of bullets: {len(bullets)}")
        print(f"Number of asteroids: {len(asteroids)}")
        
        updatable.update(dt)
        collisions = pygame.sprite.groupcollide(bullets, asteroids, True, False)
        for bullet, asteroid_list in collisions.items():
            for asteroid in asteroid_list:
                asteroid.split()
        print(f"Collisions detected: {collisions}")  # See if any collisions are happening
        
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


    