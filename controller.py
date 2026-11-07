"""Coordinates devices. The rover decision algorithm is not yet defined."""


class RoverController:
    def __init__(self, motors, buzzer, display):
        self.motors = motors
        self.buzzer = buzzer
        self.display = display

    def run(self):
        raise NotImplementedError("Define rover behavior and command input before implementation.")

    def run_demo(self):
        """Device smoke demonstration, not the rover operating algorithm."""
        self.motors.stop()
        for status in ("Detected", "Clean", "Moving"):
            self.display.show_status(status)
        print("[DEMO] Structure ready; no autonomous algorithm configured.")
