"""The simulation."""
from math import pi
from random import random
import pygame
from flock_dynamics.fish import Fish
from flock_dynamics.school import School


def update_speed_and_angle(school: School, fish: Fish):
    """Update the speed and angle of this fish."""
    nearest_neighbors = school.get_nearest_neighbors(fish)
    closest_neighbor = nearest_neighbors[0]
    angle = fish.get_direction_to_other_fish(closest_neighbor)
    distance = fish.get_distance_to_other_fish(closest_neighbor)
    if distance > 20:
        fish.set_angle(angle)
    else:
        fish.set_angle(closest_neighbor.angle)


def simulation_step(screen: pygame.Surface,
                    school: School):
    """Take another simulation step."""
    for fish in school.get_fish():
        update_speed_and_angle(school, fish)
        fish.update()
        fish.draw(screen)
