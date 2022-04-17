import math
import pygame

FPS = 30


class Fish():
    """A fish."""

    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 angle: float = 0,
                 speed: float = 1):
        self.angle = angle
        self.target_angle = angle
        self.speed = speed
        self.target_speed = speed
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
        self.target_speed = speed

    def set_angle(self, angle: float):
        """Set the angle of the fish."""
        self.target_angle = angle

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

    def update(self, width: float, height: float):
        """Update speed and angle of fish."""
        if self.target_angle > self.angle:
            self.angle += min(2 * math.pi / FPS,
                              self.target_angle - self.angle)
        else:
            self.angle -= min(2 * math.pi / FPS,
                              self.angle - self.target_angle)

        # TODO: "Slowly" increase the speed. This will require
        # information on game clock.
        self.speed = self.target_speed

        start = (self.start[0] + self.speed * math.cos(self.angle),
                 self.start[1] + self.speed * math.sin(self.angle))
        end = (start[0] + 10 * math.cos(self.angle),
               start[1] + 10 * math.sin(self.angle))
        if min([start[0], end[0]]) < 0:
            self.target_angle = (math.pi - self.target_angle) % (2 * math.pi)
            self.angle = (math.pi - self.angle) % (2 * math.pi)
        if min([start[1], end[1]]) < 0:
            self.target_angle = -self.target_angle
            self.angle = -self.angle
        if max(start[0], end[0]) > width:
            self.target_angle = (math.pi - self.target_angle) % (2 * math.pi)
            self.angle = (math.pi - self.angle) % (2 * math.pi)
        if max(start[1], end[1]) > height:
            self.target_angle = -self.target_angle
            self.angle = -self.angle
        self.start = start
        self.end = end

    def draw(self, screen: pygame.Surface):
        """Draw the screen."""
        pygame.draw.line(surface=screen, color='white',
                         start_pos=self.start, end_pos=self.end,
                         width=1)
