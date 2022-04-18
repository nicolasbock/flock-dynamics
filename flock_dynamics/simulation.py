"""The simulation."""
import math
from random import random
import pygame
from flock_dynamics.fish import Fish
from flock_dynamics.school import School


def update_speed_and_angle(school: School, fish: Fish):
    """Update the speed and angle of this fish."""
    if len(school.school) == 1:
        fish.set_speed(1)
        fish.set_angle(2 * math.pi * random())  # nosec
        return

    nearest_fish = school.get_nearest_neighbors(fish, k=2)
    distance, angle = (fish.get_distance_to_other_fish(nearest_fish[0]),
                       fish.get_direction_to_other_fish(nearest_fish[0]))
    if distance > 10:
        fish.set_speed(3)
        fish.set_angle(angle)
    else:
        fish.set_speed(1)
        fish.set_angle(angle + math.pi / 2)


def simulation_step(screen: pygame.Surface,
                    school: School,
                    width: float,
                    height: float):
    """Take another simulation step."""
    for fish in school.get_fish():
        update_speed_and_angle(school, fish)
        fish.update(width, height)
        fish.draw(screen)
