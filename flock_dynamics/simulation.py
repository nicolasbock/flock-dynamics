import pygame
import sys

from flock_dynamics.bird import Bird


def start_simulation(options):
    """The main simulation."""
    pygame.init()

    size = width, height = options.width, options.height

    screen = pygame.display.set_mode(size)

    bird = Bird(options.width / 2, options.height / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(blue)
        pygame.draw.line(surface=screen, color=white,
                         start_pos=(10, 10), end_pos=(20, 11),
                         width=1)
        pygame.display.flip()
