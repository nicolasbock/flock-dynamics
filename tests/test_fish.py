"""Unit tests for Fish"""

import unittest
from flock_dynamics.fish import Fish


class TestFish(unittest.TestCase):
    """Tests for Fish."""

    def is_fish_equal(self, fish_1: Fish, fish_2: Fish, msg: str = ''):
        """Compare two Fish."""
        if fish_1 != fish_2:
            if msg == '':
                msg = f'Fish {fish_1} and {fish_2} are not equal'
            raise self.failureException(msg)

    def setUp(self) -> None:
        self.addTypeEqualityFunc(Fish, self.is_fish_equal)

    def test_fish(self):
        """Test a random Fish."""
        self.assertEqual(Fish(), Fish(0, 0))
        self.assertEqual(Fish(2, 3), Fish(2, 3))

    def test_set_speed(self):
        """Test set the speed."""
        fish = Fish(speed=4)
        self.assertEqual(fish.speed, 4)
        fish.set_speed(5)
        self.assertEqual(fish.speed, 5)

    def test_set_angle(self):
        """Test set the angle."""
        fish = Fish(angle=0.1)
        self.assertEqual(fish.angle, 0.1)
        fish.set_angle(0.2)
        self.assertEqual(fish.angle, 0.2)
