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
        fpsClock.tick(FPS)
