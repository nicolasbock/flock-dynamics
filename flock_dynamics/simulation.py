"""The simulation."""
import pygame
import math
from random import random
from flock_dynamics.fish import Fish
from flock_dynamics.school import School


def update_position(fish: Fish, width: float, height: float):
    """Update the fish."""
    fish.set_angle(fish.angle + 0.1 * (random() - 0.5))  # nosec
    start = (fish.start[0] + fish.speed * math.cos(fish.angle),
             fish.start[1] + fish.speed * math.sin(fish.angle))
    end = (start[0] + 10 * math.cos(fish.angle),
           start[1] + 10 * math.sin(fish.angle))
    if min([start[0], end[0]]) < 0:
        fish.angle = (math.pi - fish.angle) % (2 * math.pi)
    if min([start[1], end[1]]) < 0:
        fish.angle = -fish.angle
    if max(start[0], end[0]) > width:
        fish.angle = (math.pi - fish.angle) % (2 * math.pi)
    if max(start[1], end[1]) > height:
        fish.angle = -fish.angle
    fish.start = start
    fish.end = end


def simulation_step(screen: pygame.Surface,
                    school: School,
                    width: float,
                    height: float):
    """Take another simulation step."""
    for fish in school.get_fish():
        update_position(fish, width, height)
        fish.draw(screen)
