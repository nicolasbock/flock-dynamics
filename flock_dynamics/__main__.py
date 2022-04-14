"""The main function."""

import argparse
from random import random
import pygame
from flock_dynamics.bird import Bird
from flock_dynamics.simulation import simulate

FPS = 30  # frames per second


def parse_commandline():
    """Parse the command line."""
    parser = argparse.ArgumentParser(prog='flock-dynamics')
    parser.add_argument(
        "--width",
        type=int,
        default=1280,
        help="The width of the simulation window (default %(default)s)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=720,
        help="The height of the simulation window (default %(default)s)",
    )
    return parser.parse_args()


def start_simulation(options):
    """The main simulation."""
    pygame.init()
    fps_clock = pygame.time.Clock()
    size = width, height = options.width, options.height

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Flock Dynamics')

    birds = [Bird(options.width * random(),  # nosec
                  options.height * random(),  # nosec
                  angle=0.2, speed=4)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('blue')
        simulate(screen, birds, width, height)
        pygame.display.flip()
        fps_clock.tick(FPS)


def main():
    """The main entry point."""
    options = parse_commandline()
    start_simulation(options)


if __name__ == "__main__":
    main()
