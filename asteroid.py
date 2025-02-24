import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if hasattr(self, 'containers'):
            self.groups = self.containers
            pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (self.position.x, self.position.y), self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current one
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Make the new asteroids move faster (multiply by 1.2)
        velocity1 *= 1.2
        velocity2 *= 1.2

        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at the same position as the original
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities
        new_asteroid1.velocity = velocity1
        new_asteroid2.velocity = velocity2

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        self.rect.center = (self.position.x, self.position.y)
        