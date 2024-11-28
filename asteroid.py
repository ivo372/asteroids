import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y , radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        Vector01 = self.velocity.rotate(random_angle)
        Vector02 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid01 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid02 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid01.velocity = Vector01 * 1.2
        asteroid02.velocity = Vector02 * 1.2