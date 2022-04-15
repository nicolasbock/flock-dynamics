import math
from random import random
from flock_dynamics.fish import Fish


class School():
    """A school of fish."""

    def __init__(self,
                 school_size: int,
                 width: float,
                 height: float):
        """Initialize the school."""
        self.school = []
        for _ in range(school_size):
            self.school.append(
                Fish(width * random(),  # nosec
                     height * random(),  # nosec
                     angle=2 * math.pi * random(),
                     speed=2 + 2 * random()))

    def get_fish(self) -> list[Fish]:
        """Get a list of the fish in this school."""
        return self.school

    def get_nearest_neighbors(self, fish: Fish, k: int = 1) -> list[Fish]:
        """Get the k nearsest neighbors of this fish."""
        return [fish]
