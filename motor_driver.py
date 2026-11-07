"""Motor control interface: one L298N channel per pair of motors."""

import math


class MotorDriver:
    """Demo implementation; hardware backend will be implemented separately."""

    def __init__(self, *, demo=True):
        if not demo:
            raise NotImplementedError("Motor GPIO backend is not implemented yet.")
        self.left_speed = 0.0
        self.right_speed = 0.0

    def drive(self, left, right):
        """Signed duty cycles: -1 reverse, 0 stop, +1 forward."""
        for speed in (left, right):
            if (isinstance(speed, bool) or not isinstance(speed, (int, float))
                    or not math.isfinite(speed) or not -1 <= speed <= 1):
                raise ValueError("Motor duty cycles must be finite numbers from -1 to 1.")
        self.left_speed, self.right_speed = float(left), float(right)
        print(f"[DEMO motor] left={left:+.2f}, right={right:+.2f}")

    def stop(self):
        self.drive(0, 0)

    def close(self):
        self.stop()
