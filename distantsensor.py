"""HC-SR04-style ultrasonic distance readings in centimeters.

Run directly: python3 distantsensor.py [--demo].
"""

import argparse
from time import monotonic, sleep

from config import DISTANCE_ECHO_PIN, DISTANCE_TRIGGER_PIN


class distantSensor:
    """Measure trigger/echo pulse duration, with bounded waits for missing echoes.

    Demo mode reports an explicitly simulated 100 cm. Hardware timing uses
    Python polling and is approximate; Linux scheduling can affect accuracy.
    """

    def __init__(self, *, demo=True, trigger=DISTANCE_TRIGGER_PIN,
                 echo=DISTANCE_ECHO_PIN):
        self.demo = demo
        self._trigger = None
        self._echo = None
        self._closed = False
        if not demo:
            from gpiozero import DigitalInputDevice, DigitalOutputDevice

            try:
                self._trigger = DigitalOutputDevice(trigger, initial_value=False)
                self._echo = DigitalInputDevice(echo, pull_up=False)
                sleep(0.1)
            except Exception:
                self.close()
                raise
        mode = "DEMO" if demo else "HARDWARE"
        print(f"[{mode} distance] initialized: Trigger BCM {trigger}, Echo BCM {echo}",
              flush=True)

    def readDistance(self):
        """Return centimeters, or None if Echo times out. Space calls >=60 ms apart."""
        if self._closed:
            raise RuntimeError("Distance sensor is closed.")
        if self.demo:
            return 100.0
        # A high Echo before triggering indicates a stale/stuck pulse.
        if self._echo.value:
            return None
        self._trigger.on()
        try:
            sleep(0.00001)
        finally:
            self._trigger.off()

        deadline = monotonic() + 0.03
        while not self._echo.value:
            if monotonic() >= deadline:
                return None
        start = monotonic()
        deadline = start + 0.03
        while self._echo.value:
            if monotonic() >= deadline:
                return None
        # Sound travels to the object and back; 34300 cm/s is approximate.
        return (monotonic() - start) * 34300 / 2

    def run(self):
        """Print a distance every approximately 0.5 seconds until interrupted."""
        mode = "DEMO" if self.demo else "HARDWARE"
        while True:
            started = monotonic()
            distance = self.readDistance()
            result = "no valid echo" if distance is None else f"{distance:.1f} cm"
            if self.demo:
                result += " (simulated)"
            print(f"[{mode} distance] {result}", flush=True)
            sleep(max(0, 0.5 - (monotonic() - started)))

    def close(self):
        """Release both GPIO pins; safe to call repeatedly."""
        if self._closed:
            return
        try:
            if self._trigger is not None:
                self._trigger.close()
        finally:
            if self._echo is not None:
                self._echo.close()
            self._closed = True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="Log simulated readings without GPIO")
    args = parser.parse_args()
    sensor = distantSensor(demo=args.demo)
    try:
        sensor.run()
    except KeyboardInterrupt:
        print("Stopping distance readings.")
    finally:
        sensor.close()
