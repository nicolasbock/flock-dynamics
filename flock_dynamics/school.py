"""A school of fish."""

import math
from random import random
from flock_dynamics.fish import Fish
from flock_dynamics.global_parameters import SimulationParameters


class School():
    """A school of fish."""

    def __init__(self, school_size: int = 1):
        """Initialize the school."""
        if school_size < 0:
            raise Exception(
                'School size has to be greater than or equal to 0!')

        self.school = []
        for _ in range(school_size):
            self.school.append(
                Fish(SimulationParameters.WIDTH * random(),  # nosec
                     SimulationParameters.HEIGHT * random(),  # nosec
                     angle=2 * math.pi * random(),
                     speed=2 + 2 * random()))

    def add_fish(self, fish: Fish):
        """Add a fish to the school."""
        self.school.append(fish)

    def get_fish(self) -> list[Fish]:
        """Get a list of the fish in this school."""
        return self.school

    def get_nearest_neighbors(self, fish: Fish, k: int = 1) -> list[Fish]:
        """Get the k nearsest neighbors of this fish."""
        distances: list[tuple[int, float]] = []
        for i, other_fish in enumerate(self.school):
            distances.append(
                (i,
                 (fish.start[0] - other_fish.start[0])**2 +
                 (fish.start[1] - other_fish.start[1])**2))
        k = min(len(self.school), k)
        sorted_distances = sorted(distances, key=lambda item: item[1])[1:1 + k]
        return [self.school[item[0]] for item in sorted_distances]
