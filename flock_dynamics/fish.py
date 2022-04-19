import math
import pygame
from flock_dynamics.global_parameters import SimulationParameters


class Fish():
    """A fish."""

    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 angle: float = 0,
                 speed: float = 1):

        self.angle: float = angle
        self.target_angle: float = angle
        self.speed: float = speed
        self.target_speed: float = speed

        self.start: tuple[float, float] = (x, y)
        self.end: tuple[float, float] = \
            (self.start[0] +
             SimulationParameters.FISH_LENGTH * math.sin(self.angle),
             self.start[1] +
             SimulationParameters.FISH_LENGTH * math.cos(self.angle))

        self.enforce_boundary()

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

    def enforce_boundary(self):
        """Check that the fish is inside the box and stays there."""
        if self.start[0] < 0 or self.end[0] < 0:
            shift = max(-self.start[0], -self.end[0])
            self.start = (self.start[0] + shift, self.start[1])
            self.end = (self.end[0] + shift, self.end[1])
        if self.start[1] < 0 or self.end[1] < 0:
            shift = max(-self.start[1], -self.end[1])
            self.start = (self.start[0], self.start[1] + shift)
            self.end = (self.end[0], self.end[1] + shift)
        if self.start[0] > SimulationParameters.WIDTH or \
                self.end[0] > SimulationParameters.WIDTH:
            shift = max(self.start[0] - SimulationParameters.WIDTH,
                        self.end[0] - SimulationParameters.WIDTH)
            self.start = (self.start[0] + shift, self.start[1])
            self.end = (self.end[0] + shift, self.end[1])
        if self.start[1] > SimulationParameters.HEIGHT or \
                self.end[1] > SimulationParameters.HEIGHT:
            shift = max(self.start[1] - SimulationParameters.HEIGHT,
                        self.end[1] - SimulationParameters.HEIGHT)
            self.start = (self.start[0], self.start[1] + shift)
            self.end = (self.end[0], self.end[1] + shift)

    def set_speed(self, speed: float):
        """Set the target speed of the fish."""
        self.target_speed = speed

    def set_angle(self, angle: float):
        """Set the angle of the fish."""
        self.target_angle = angle

    def get_distance_to_other_fish(self, other) -> float:
        """Get the distance to another fish."""
        return math.sqrt(
            (self.start[0] - other.start[0])**2 +
            (self.start[1] - other.start[1])**2)

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

    def update(self):
        """Update speed and angle of fish."""
        prefactor = +1
        if self.target_angle < self.angle:
            prefactor = -1
        self.angle += prefactor * \
            min(2 * math.pi / SimulationParameters.FPS,
                math.fabs(self.target_angle - self.angle))

        prefactor = +1
        if self.target_speed < self.speed:
            prefactor = -1
        self.speed += prefactor * \
            min(2 / SimulationParameters.FPS,
                math.fabs(self.target_speed - self.speed))

        # Advance fish in time.
        self.start = (self.start[0] + self.speed * math.cos(self.angle),
                      self.start[1] + self.speed * math.sin(self.angle))
        self.end = (self.start[0] +
                    SimulationParameters.FISH_LENGTH * math.cos(self.angle),
                    self.start[1] +
                    SimulationParameters.FISH_LENGTH * math.sin(self.angle))
        self.enforce_boundary()

    def draw(self, screen: pygame.Surface):
        """Draw the screen."""
        pygame.draw.line(surface=screen, color='white',
                         start_pos=self.start,
                         end_pos=self.end,
                         width=1)
        pygame.draw.circle(surface=screen,
                           color='red',
                           center=self.start,
                           radius=3)
