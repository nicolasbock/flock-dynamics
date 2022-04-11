import pygame
import sys

from flock_dynamics.bird import Bird

FPS = 30 # frames per second

def start_simulation(options):
    """The main simulation."""
    pygame.init()
    fpsClock = pygame.time.Clock()
    size = width, height = options.width, options.height

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Flock Dynamics')

    birds = [Bird(options.width / 2, options.height / 2, angle=0.2, speed=0.5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('blue')
        for bird in birds:
            bird.update(width, height)
            bird.draw(screen)
        pygame.display.flip()
        fpsClock.tick(FPS)
