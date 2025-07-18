import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.radius = radius
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):

        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.radius *= 0.5
            new_asteroid = Asteroid(self.position.x,self.position.y,self.radius)

            angle = random.uniform(10,30)
            old_velocity = self.velocity
            self.velocity = old_velocity.rotate(angle) * 1.2
            new_asteroid.velocity = old_velocity.rotate(-angle) * 1.2

