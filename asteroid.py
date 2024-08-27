import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius, velocity=None):
    super().__init__(x, y, radius)
    self.position = pygame.Vector2(x, y)
    self.radius = radius
    self.velocity = velocity or pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * 100

  def draw(self, screen):
    pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
    
    if self.position.x < 0:
      self.position.x = SCREEN_WIDTH
    elif self.position.x > SCREEN_WIDTH:
      self.position.x = 0
        
    if self.position.y < 0:
      self.position.y = SCREEN_HEIGHT
    elif self.position.y > SCREEN_HEIGHT:
      self.position.y = 0

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    random_angle = random.uniform(20, 50)

    new_radius = self.radius - ASTEROID_MIN_RADIUS

    velocity1 = self.velocity.rotate(random_angle) * 1.2
    velocity2 = self.velocity.rotate(-random_angle) * 1.2

    new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, velocity1)
    new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, velocity2)

    self.containers[0].add(new_asteroid1)
    self.containers[0].add(new_asteroid2)
    self.containers[1].add(new_asteroid1)
    self.containers[1].add(new_asteroid2)