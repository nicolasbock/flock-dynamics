import argparse
from flock_dynamics.simulation import start_simulation


def parse_commandline():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main():
    options = parse_commandline()
    start_simulation(options)
