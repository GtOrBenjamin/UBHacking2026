"""PWM piezo buzzer interface, independent of rover behavior."""

import math
from time import sleep

from config import BUZZER_PIN


class Buzzer:
    """Play tones on a passive piezo buzzer, or simulate them in demo mode."""

    def __init__(self, *, demo=True, pin=BUZZER_PIN):
        self.demo = demo
        self.frequency = None
        self._device = None
        if not demo:
            if pin is None:
                raise ValueError("Set BUZZER_PIN in config.py before hardware playback.")
            # Keep demo mode independent of Raspberry Pi libraries.
            from gpiozero import PWMOutputDevice

            self._device = PWMOutputDevice(pin, initial_value=0, frequency=440)

    def tone(self, frequency):
        """Start a continuous tone; caller controls when to stop it."""
        if (isinstance(frequency, bool) or not isinstance(frequency, (int, float))
                or not math.isfinite(frequency) or frequency <= 0):
            raise ValueError("Tone frequency must be a positive finite number in Hz.")
        if self.demo:
            print(f"[DEMO buzzer] {frequency} Hz")
        else:
            self._device.value = 0
            self._device.frequency = frequency
            self._device.value = 0.5
        self.frequency = frequency

    def playingSound(self, notes):
        """Play (frequency_hz, duration_seconds) pairs synchronously.

        Frequency 0 is a silent rest. Durations must be nonnegative.
        Validate the entire melody before playing; always turn off on exit.
        Demo mode prints notes and waits for their durations without GPIO.
        """
        HPBD = [
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
            (523, 1.0)
        ]

        try:
            melody = HPBD
            for note in notes:
                if not isinstance(note, (tuple, list)) or len(note) != 2:
                    raise ValueError("Each note must be a (frequency, duration) pair.")
                frequency, duration = note
                for value in (frequency, duration):
                    if (isinstance(value, bool) or not isinstance(value, (int, float))
                            or not math.isfinite(value) or value < 0):
                        raise ValueError(
                            "Frequency and duration must be finite nonnegative numbers."
                        )
                melody.append((frequency, duration))

            for frequency, duration in melody:
                if duration == 0:
                    continue
                if frequency == 0:
                    self.off()
                else:
                    self.tone(frequency)
                sleep(duration)
                self.off()
        finally:
            self.off()

    def off(self):
        if self._device is not None:
            self._device.off()
        self.frequency = None
        if self.demo:
            print("[DEMO buzzer] off")

    def close(self):
        try:
            self.off()
        finally:
            if self._device is not None:
                self._device.close()
                self._device = None
