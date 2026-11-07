
"""Rover entry point. Run with real hardware by default."""

import argparse
from contextlib import ExitStack

from buzzer import Buzzer
from controller import RoverController


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run without accessing GPIO hardware"
    )
    args = parser.parse_args()

    # Default: real hardware
    demo = args.demo

    with ExitStack() as cleanup:
        buzzer = Buzzer(demo=demo)
        cleanup.callback(buzzer.close)

        controller = RoverController(buzzer)

        try:
            if demo:
                controller.run_demo()
            else:
                controller.run()
        except KeyboardInterrupt:
            print("Stopping rover.")


if __name__ == "__main__":
    main()
