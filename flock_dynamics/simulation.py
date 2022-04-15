"""The simulation."""
import pygame
from flock_dynamics.fish import Fish


def simulate(screen: pygame.Surface,
             school: list[Fish],
             width: float,
             height: float):
    """Take another simulation step."""
    for fish in school:
        fish.update_position(width, height)
        fish.draw(screen)
