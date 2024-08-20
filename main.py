import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    
    keepRunningGame = True
    while keepRunningGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
            
        for thing in updatable:
            thing.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print('Game Over')
                sys.exit()
            
        screen.fill('black')
        
        for thing in drawable:
            thing.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()