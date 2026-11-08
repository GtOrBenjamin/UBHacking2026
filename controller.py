"""Coordinates the rover's distance sensor, buzzer, and LCD display."""
from distantsensor import distantSensor

class RoverController:
    def __init__(self, buzzer, lcd, *, demo=True):
        self.buzzer = buzzer
        self.lcd = lcd
        self.distance_sensor = distantSensor(demo=demo)

    def runDistance(self):
        """Print sensor readings every 0.5 seconds until interrupted."""
        self.distance_sensor.run()

    def run(self):
        """Continuously show distance readings in the configured mode."""
        self.lcd.writeFirstLine("Rover ready")
        self.lcd.writeSecondLine("Reading distance")
        self.runDistance()

    def close(self):
        """Release the sensor owned by this controller."""
        self.distance_sensor.close()

    def playMelody(self):
        """Play the existing melody when explicitly requested."""
        melody = [
            (466, 0.1), (0, 0.03), (466, 0.1), (0, 0.03), (415, 0.1), (0, 0.03), (415, 0.1), (0, 0.03),
            (698, 0.3), (0, 0.09), (698, 0.3), (0, 0.09), (622, 0.6), (0, 0.18), (466, 0.1), (0, 0.03),
            (466, 0.1), (0, 0.03), (415, 0.1), (0, 0.03), (415, 0.1), (0, 0.03), (622, 0.3), (0, 0.09),
            (622, 0.3), (0, 0.09), (554, 0.3), (0, 0.09), (523, 0.1), (0, 0.03), (466, 0.2), (0, 0.06),
            (554, 0.1), (0, 0.03), (554, 0.1), (0, 0.03), (554, 0.1), (0, 0.03), (554, 0.1), (0, 0.03),
            (554, 0.3), (0, 0.09), (622, 0.3), (0, 0.09), (523, 0.3), (0, 0.09), (466, 0.1), (0, 0.03),
            (415, 0.2), (0, 0.06), (415, 0.2), (0, 0.06), (415, 0.2), (0, 0.06), (622, 0.4), (0, 0.12),
            (554, 0.8), (0, 0.24), (466, 0.1), (0, 0.03), (466, 0.1), (0, 0.03), (415, 0.1), (0, 0.03),
            (415, 0.1), (0, 0.03), (698, 0.3), (0, 0.09), (698, 0.3), (0, 0.09), (622, 0.6), (0, 0.18),
            (466, 0.1), (0, 0.03), (466, 0.1), (0, 0.03), (415, 0.1), (0, 0.03), (415, 0.1), (0, 0.03),
            (831, 0.3), (0, 0.09), (523, 0.3), (0, 0.09), (554, 0.3), (0, 0.09), (523, 0.1), (0, 0.03),
            (466, 0.2), (0, 0.06), (554, 0.1), (0, 0.03), (554, 0.1), (0, 0.03), (554, 0.1), (0, 0.03),
            (554, 0.1), (0, 0.03), (554, 0.3), (0, 0.09), (622, 0.3), (0, 0.09), (523, 0.3), (0, 0.09),
            (466, 0.1), (0, 0.03), (415, 0.2), (0, 0.06), (0, 0.2), (0, 0.06), (415, 0.2), (0, 0.06),
            (622, 0.4), (0, 0.12), (554, 0.8), (0, 0.24), (0, 0.4), (0, 0.12),
        ]
        self.lcd.writeFirstLine("Rover ready")
        self.lcd.writeSecondLine("Playing melody")
        # self.buzzer.playingSound(melody)
        

    def run_demo(self):
        """Run distance reporting using the demo sensor."""
        self.run()
