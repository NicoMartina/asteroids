import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #SETS THE COLOR OF THE WINDOW
        updatable.update(dt)
        screen.fill("black")
        drawable.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    
if __name__ == "__main__":
    main()