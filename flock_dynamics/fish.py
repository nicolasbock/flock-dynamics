import math
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

    def __str__(self) -> str:
        return f'Fish f{id(self)} at ({self.start[0]}, {self.start[1]})'

    def __repr__(self) -> str:
        return f'Fish(x={self.start[0]}, y={self.start[1]}, ' \
            + f'angle={self.angle}, speed={self.speed})'

    def set_speed(self, speed: float):
        """Set the target speed of the bird."""
        # TODO: "Slowly" increase the speed. This will require
        # information on game clock.
        self.speed = speed

    def set_angle(self, angle: float):
        """Set the angle of the Bird."""
        # TODO: "Slowly" update angle.
        self.angle = angle

    def draw(self, screen: pygame.Surface):
        """Draw the screen."""
        pygame.draw.line(surface=screen, color='white',
                         start_pos=self.start, end_pos=self.end,
                         width=1)
