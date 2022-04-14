import math
from random import random
import pygame


class Bird():
    """A bird."""

    def __init__(self, x=0, y=0, angle=0, speed=1):
        self.angle = angle
        self.speed = speed
        self.start = (x, y)
        self.end = (self.start[0] + 10 * math.sin(self.angle),
                    self.start[1] + 10 * math.cos(self.angle))

    def update(self, width, height):
        """Update the birds."""
        self.angle += 0.1 * (random() - 0.5)  # nosec
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

    def draw(self, screen):
        """Draw the screen."""
        pygame.draw.line(surface=screen, color='white',
                         start_pos=self.start, end_pos=self.end,
                         width=1)
