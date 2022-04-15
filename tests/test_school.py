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


if __name__ == '__main__':
    unittest.main()
