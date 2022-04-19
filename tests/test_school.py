"""Tests"""

import unittest
import math
from flock_dynamics.global_parameters import SimulationParameters
from flock_dynamics.fish import Fish
from flock_dynamics.school import School


class TestSchool(unittest.TestCase):
    """Test the School class."""
    def setUp(self) -> None:
        SimulationParameters.WIDTH = 500
        SimulationParameters.HEIGHT = 500
        fishies = [
            (3, 90),
            (0, 0),
            (5, 73),
            (8, 181),
            (12, 220),
            (15, 330),
        ]
        self.fishies = [
            Fish(100 + r * math.cos(angle * math.pi / 180),
                 100 + r * math.sin(angle * math.pi / 180))
            for r, angle in fishies
        ]
        self.school: School = School(school_size=0)
        for fish in self.fishies:
            self.school.add_fish(fish)

    def test_nearest_neighbors_1(self):
        """Test the nearest neighbor list."""
        nearest_neighbors = self.school.get_nearest_neighbors(self.fishies[1])
        self.assertEqual(nearest_neighbors[0], self.fishies[0])
        self.assertEqual(len(nearest_neighbors), 1)

    def test_nearest_neighbors_2(self):
        """Test the nearest neighbor list."""
        nearest_neighbors = self.school.get_nearest_neighbors(
            self.fishies[1], k=2)
        self.assertEqual(nearest_neighbors[0], self.fishies[0])
        self.assertEqual(nearest_neighbors[1], self.fishies[2])
        self.assertEqual(len(nearest_neighbors), 2)

    def test_add_fish(self):
        """Test adding a fish to the school."""
        new_fish = Fish(20, 20)
        self.school.add_fish(new_fish)
        self.assertEqual(self.school.get_fish()[-1], new_fish)

    def test_get_fish(self):
        """Test getting the fishies."""
        fishies = self.school.get_fish()
        for i, fish in enumerate(fishies):
            self.assertEqual(fish, self.fishies[i])


if __name__ == '__main__':
    unittest.main()
