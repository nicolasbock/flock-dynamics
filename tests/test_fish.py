"""Unit tests for Fish"""

import unittest
import math
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
        self.assertEqual(fish.target_speed, 4)
        fish.set_speed(5)
        self.assertEqual(fish.speed, 4)
        self.assertEqual(fish.target_speed, 5)

    def test_set_angle(self):
        """Test set the angle."""
        fish = Fish(angle=0.1)
        self.assertEqual(fish.angle, 0.1)
        self.assertEqual(fish.target_angle, 0.1)
        fish.set_angle(0.2)
        self.assertEqual(fish.angle, 0.1)
        self.assertEqual(fish.target_angle, 0.2)

    def test_update(self):
        """Test the update method."""
        fish = Fish()
        fish.set_angle(1.8)
        self.assertEqual(fish.angle, 0)
        self.assertEqual(fish.target_angle, 1.8)
        fish.update(100, 100)
        self.assertAlmostEqual(fish.angle, 2 * math.pi / 30)

    def test_get_distance(self):
        """Test the distance util method."""
        fish_1 = Fish(0, 0)
        fish_2 = Fish(3, 10)
        self.assertEqual(fish_1.get_distance_to_other_fish(fish_2),
                         math.sqrt(3**2 + 10**2))

    def test_get_direction(self):
        """Test the direction to other fish."""
        fish = Fish(0, 0)
        angles = [
            0,
            0.3,
            math.pi / 2,
            1.9, math.pi,
            3.5,
            3 / 2 * math.pi,
            5.4,
            2 * math.pi,
            7,
            ]
        for angle in angles:
            self.assertAlmostEqual(
                fish.get_direction_to_other_fish(
                    Fish(math.cos(angle), math.sin(angle))),
                angle % (2 * math.pi))
