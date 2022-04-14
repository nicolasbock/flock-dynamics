"""The simulation."""


def simulate(screen, birds, width, height):
    """Take another simulation step."""
    for bird in birds:
        bird.update(width, height)
        bird.draw(screen)
