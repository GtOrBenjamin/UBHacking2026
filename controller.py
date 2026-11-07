"""Coordinates buzzer behavior."""

class RoverController:
    def __init__(self, buzzer):
        self.buzzer = buzzer

    def run(self):
        """Play an example melody using the configured buzzer mode."""
        self.buzzer.playingSound([
            (440, 0.3),
            (494, 0.3),
            (523, 0.6),
            (0, 0.2),
            (523, 0.3),
            (440, 0.6),
        ])

    def run_demo(self):
        """Simulate the same melody when main constructs a demo buzzer."""
        self.run()
