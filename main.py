"""Rover entry point. Run a hardware-free demo: python main.py --demo."""

import argparse
from contextlib import ExitStack

from buzzer import Buzzer
from controller import RoverController
from lcd_display import LCDDisplay
from motor_driver import MotorDriver


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", required=True,
                        help="Run the module demonstration without GPIO access")
    parser.parse_args()

    # Register cleanup immediately after each device initializes. ExitStack
    # attempts all callbacks even when initialization or another callback fails.
    with ExitStack() as cleanup:
        display = LCDDisplay(demo=True)
        cleanup.callback(display.close)
        buzzer = Buzzer(demo=True)
        cleanup.callback(buzzer.close)
        motors = MotorDriver(demo=True)
        cleanup.callback(motors.close)
        controller = RoverController(motors, buzzer, display)
        try:
            controller.run_demo()
        except KeyboardInterrupt:
            print("Stopping rover.")


if __name__ == "__main__":
    main()
