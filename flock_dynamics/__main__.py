import argparse
from flock_dynamics.simulation import start_simulation


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


def main():
    """The main entry point."""
    options = parse_commandline()
    start_simulation(options)


if __name__ == "__main__":
    main()
