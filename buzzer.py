"""PWM piezo buzzer interface, independent of rover behavior."""

import math


class Buzzer:
    """Demo implementation; GPIO and wiring are not yet specified."""

    def __init__(self, *, demo=True):
        if not demo:
            raise NotImplementedError("Buzzer GPIO and hardware backend are pending.")
        self.frequency = None

    def tone(self, frequency):
        """Start a continuous tone; caller controls when to stop it."""
        if (isinstance(frequency, bool) or not isinstance(frequency, (int, float))
                or not math.isfinite(frequency) or frequency <= 0):
            raise ValueError("Tone frequency must be a positive finite number in Hz.")
        self.frequency = frequency
        print(f"[DEMO buzzer] {frequency} Hz")

    def off(self):
        self.frequency = None
        print("[DEMO buzzer] off")

    def close(self):
        self.off()
