import pygame
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill() 
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,  # The surface to draw on
            "white",  # The color of the circle
            (int(self.position.x), int(self.position.y)),  # Center position (cast to integers for screen drawing)
            self.radius  # Radius of the circle
        )