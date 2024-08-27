from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.position = pygame.Vector2(x, y)
    self.rotation = 0
    self.shoot_timer = 0
    self.invulnerable = False
    self.velocity = pygame.Vector2(0, 0)
    self.acceleration = 500
    self.max_speed = 300
    
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    color = "#FFFFFF" if not self.invulnerable else "#FFFF00"
    pygame.draw.polygon(screen, color, self.triangle(), 2)
    
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt
    
  def update(self, dt):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
      self.rotate(-dt)
    
    if keys[pygame.K_d]:
      self.rotate(dt)
    
    if keys[pygame.K_w]:
      self.move(dt)
      
    if keys[pygame.K_s]:
      self.move(-dt)
      
    if keys[pygame.K_SPACE]:
      self.shoot()
      
    if self.shoot_timer > 0:
      self.shoot_timer -= dt
      
    self.position += self.velocity * dt
    
    if self.position.x < 0:
      self.position.x = SCREEN_WIDTH
    elif self.position.x > SCREEN_WIDTH:
      self.position.x = 0
        
    if self.position.y < 0:
      self.position.y = SCREEN_HEIGHT
    elif self.position.y > SCREEN_HEIGHT:
      self.position.y = 0
    
  def apply_acceleration(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.velocity += forward * self.acceleration * dt
    if self.velocity.length() > self.max_speed:
      self.velocity.scale_to_length(self.max_speed)
      
  def apply_deceleration(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    deceleration = 0.9
    self.velocity -= forward * self.acceleration * dt * deceleration
    if self.velocity.length() < 0.1:
      self.velocity = pygame.Vector2(0, 0)
  
  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt
    
  def shoot(self):
    if self.shoot_timer <= 0:  
      shot = Shot(self.position.x, self.position.y, self.rotation)
      self.containers[0].add(shot)
      self.containers[1].add(shot)
      self.shoot_timer = PLAYER_SHOOT_COOLDOWN