"""The simulation."""
import pygame
from flock_dynamics.bird import Bird


def simulate(screen: pygame.Surface,
             birds: list[Bird],
             width: float,
             height: float):
    """Take another simulation step."""
    for bird in birds:
        bird.update_position(width, height)
        bird.draw(screen)
