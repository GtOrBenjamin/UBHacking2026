"""Coordinates the rover's buzzer and LCD display."""
from time import sleep

class RoverController:
    def __init__(self, buzzer, lcd):
        self.buzzer = buzzer
        self.lcd = lcd

    def run(self):
        """Play Happy Birthday using the configured buzzer mode."""
        melody = [
            # Happy birthday to you
            (392, 0.25),
            (392, 0.25),
            (440, 0.5),
            (392, 0.5),
            (523, 0.5),
            (494, 1.0),

            # Happy birthday to you
            (392, 0.25),
            (392, 0.25),
            (440, 0.5),
            (392, 0.5),
            (587, 0.5),
            (523, 1.0),

            # Happy birthday dear ...
            (392, 0.25),
            (392, 0.25),
            (784, 0.5),
            (659, 0.5),
            (523, 0.5),
            (494, 0.5),
            (440, 1.0),

            # Happy birthday to you
            (698, 0.25),
            (698, 0.25),
            (659, 0.5),
            (523, 0.5),
            (587, 0.5),
            (523, 1.0),
        ]
        # self.lcd.writeFirstLine("Rover ready")
        # self.lcd.writeSecondLine("Playing melody")
        self.buzzer.playingSound(melody)
        

    def run_demo(self):
        """Simulate the same melody when main constructs a demo buzzer."""
        self.run()
