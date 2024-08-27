import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
  def __init__(self, x, y, rotation):
    super().__init__(x, y, SHOT_RADIUS)
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED

  def update(self, dt):
    self.position += self.velocity * dt

  def draw(self, screen):
    pygame.draw.circle(screen, "#FFFFFF", self.position, SHOT_RADIUS)
