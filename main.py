import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  while True:
    screen.fill("black")
    pygame.display.flip() 
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
  
if __name__ == "__main__":
  main()