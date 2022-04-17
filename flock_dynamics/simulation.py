"""The simulation."""
import pygame
from random import random
from flock_dynamics.fish import Fish
from flock_dynamics.school import School


def update_speed_and_angle(fish: Fish):
    """Update the speed and angle of this fish."""
    fish.set_speed(fish.speed)
    fish.set_angle(fish.target_angle + 0.1 * (random() - 0.5))  # nosec


def simulation_step(screen: pygame.Surface,
                    school: School,
                    width: float,
                    height: float):
    """Take another simulation step."""
    for fish in school.get_fish():
        update_speed_and_angle(fish)
        fish.update(width, height)
        fish.draw(screen)
