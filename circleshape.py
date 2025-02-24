import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        self.rect.center = (self.position.x, self.position.y)
        # sub-classes must override
        pass

    def collision(self, CircleShape):
        if self.position.distance_to(CircleShape.position) <= self.radius + CircleShape.radius:
            return True
        else:
            return False