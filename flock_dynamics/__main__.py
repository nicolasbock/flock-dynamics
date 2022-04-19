"""The main function."""

import argparse
import sys
import pygame
from flock_dynamics.global_parameters import SimulationParameters
from flock_dynamics.school import School
from flock_dynamics.simulation import simulation_step


def parse_commandline() -> argparse.Namespace:
    """Parse the command line."""
    parser = argparse.ArgumentParser(prog='flock-dynamics')
    parser.add_argument(
        '--width',
        type=int,
        default=1280,
        help='The width of the simulation window (default %(default)s)',
    )
    parser.add_argument(
        '--height',
        type=int,
        default=720,
        help='The height of the simulation window (default %(default)s)',
    )
    parser.add_argument(
        '--school-size',
        type=int,
        default=1,
        help='The number of fish in the school (default = %(default)s)',
    )
    return parser.parse_args()


def start_simulation(options: argparse.Namespace):
    """The main simulation."""
    pygame.init()
    fps_clock = pygame.time.Clock()

    size = SimulationParameters.WIDTH, SimulationParameters.HEIGHT \
        = options.width, options.height

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Flock Dynamics')

    school = School(options.school_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('blue')
        simulation_step(screen, school)
        pygame.display.flip()
        fps_clock.tick(SimulationParameters.FPS)


def main():
    """The main entry point."""
    options = parse_commandline()
    start_simulation(options)


if __name__ == "__main__":
    main()
