
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    #containers = pygame.sprite.Group()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)
        #return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt
        return super().update(dt)