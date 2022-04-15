"""Tests"""

import unittest
from flock_dynamics.fish import Fish
from flock_dynamics.school import School


class TestSchool(unittest.TestCase):
    """Test the School class."""
    def setUp(self) -> None:
        self.fishies = [
            Fish(0, 0),
            Fish(10, 0),
            Fish(10, 8),
            Fish(15, 20),
        ]
        self.school: School = School(school_size=0)
        for fish in self.fishies:
            self.school.add_fish(fish)

    def test_nearest_neighbors(self):
        """Test the nearest neighbor list."""
        nearest_neighbors = self.school.get_nearest_neighbors(self.fishies[1])
        self.assertEqual(nearest_neighbors[0], self.fishies[2])

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
