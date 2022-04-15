import math
import pygame


class Fish():
    """A fish."""

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

    def __eq__(self, other) -> bool:
        if self.start[0] == other.start[0] and \
           self.start[1] == other.start[1] and \
           self.angle == other.angle and \
           self.speed == other.speed:
            return True
        return False

    def set_speed(self, speed: float):
        """Set the target speed of the fish."""
        # TODO: "Slowly" increase the speed. This will require
        # information on game clock.
        self.speed = speed

    def set_angle(self, angle: float):
        """Set the angle of the fish."""
        # TODO: "Slowly" update angle.
        self.angle = angle

    def get_distance_to_other_fish(self, other) -> float:
        """Get the distance to another fish."""
        return math.sqrt(
            (self.start[0] - other.start[0])**2
            + (self.start[1] - other.start[1])**2)

    def get_direction_to_other_fish(self, other) -> float:
        """Get the direction (angle) to another fish."""
        x, y = (other.start[0] - self.start[0],
                other.start[1] - self.start[1])
        if y >= 0:
            if x > 10e-6:
                return math.atan(y / x)
            if x < -10e-6:
                return math.pi + math.atan(y / x)
            return math.pi / 2
        if x < -10e-6:
            return math.pi + math.atan(y / x)
        if x > 10e-6:
            return (2 * math.pi + math.atan(y / x)) % (2 * math.pi)
        return math.pi * 3 / 2

    def draw(self, screen: pygame.Surface):
        """Draw the screen."""
        pygame.draw.line(surface=screen, color='white',
                         start_pos=self.start, end_pos=self.end,
                         width=1)
