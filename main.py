import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable

  asteroid_field = AsteroidField()
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # Update objects
    for obj in updatable:
      obj.update(dt)

    # Handle bullet-asteroid collisions
    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collision(shot):
          asteroid.split()  # Replace kill with split
          shot.kill()

    # Clear screen
    screen.fill("black")

    # Draw objects
    for obj in drawable:
      obj.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Check for player-asteroid collisions
    for obj in asteroids:
      if player.collision(obj):
        print("Game over!")
        running = False

      # Cap the frame rate
    dt = clock.tick(60) / 1000
  
  pygame.quit()
    
if __name__ == "__main__":
    main()