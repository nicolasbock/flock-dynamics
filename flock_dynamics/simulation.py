import pygame
import sys

from flock_dynamics.bird import Bird


def start_simulation(options):
    """The main simulation."""
    pygame.init()

    size = width, height = options.width, options.height

    screen = pygame.display.set_mode(size)

    birds = [Bird(options.width / 2, options.height / 2, angle=0.2, speed=0.5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill('blue')
        for bird in birds:
            bird.update(width, height)
            bird.draw(screen)
        pygame.display.flip()
