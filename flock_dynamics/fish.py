import math
from random import random
import pygame


class Fish():
    """A bird."""

    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 angle: float = 0,
                 speed: float = 1):
        self.angle = angle
        self.speed = speed
        self.start = (x, y)
        self.end = (self.start[0] + 10 * math.sin(self.angle),
                    self.start[1] + 10 * math.cos(self.angle))

    def set_speed(self, speed: float):
        """Set the target speed of the bird."""
        # TODO: "Slowly" increase the speed. This will require
        # information on game clock.
        self.speed = speed

    def set_angle(self, angle: float):
        """Set the angle of the Bird."""
        # TODO: "Slowly" update angle.
        self.angle = angle

    def get_nearest_neighbors(self, k: int = 1):
        """Get the k nearsest neighbors of this bird."""
        return self

    def update_position(self, width: float, height: float):
        """Update the birds."""
        self.set_angle(self.angle + 0.1 * (random() - 0.5))  # nosec
        start = (self.start[0] + self.speed * math.cos(self.angle),
                 self.start[1] + self.speed * math.sin(self.angle))
        end = (start[0] + 10 * math.cos(self.angle),
               start[1] + 10 * math.sin(self.angle))
        if min([start[0], end[0]]) < 0:
            self.angle = (math.pi - self.angle) % (2 * math.pi)
        if min([start[1], end[1]]) < 0:
            self.angle = -self.angle
        if max(start[0], end[0]) > width:
            self.angle = (math.pi - self.angle) % (2 * math.pi)
        if max(start[1], end[1]) > height:
            self.angle = -self.angle
        self.start = start
        self.end = end

    def draw(self, screen: pygame.Surface):
        """Draw the screen."""
        pygame.draw.line(surface=screen, color='white',
                         start_pos=self.start, end_pos=self.end,
                         width=1)
