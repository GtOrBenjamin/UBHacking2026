"""Direction and PWM control for the rover's two L298N channels."""

import math

from config import MOTOR_ENA, MOTOR_ENB, MOTOR_IN1, MOTOR_IN2, MOTOR_IN3, MOTOR_IN4


class MotorDriver:
    """Control both motor pairs. Commands persist until changed or stopped.

    Speeds are percentages from 0 to 100. Demo mode never accesses GPIO.
    """

    def __init__(self, *, demo=True):
        self.demo = demo
        self._devices = []
        self._closed = False
        if not demo:
            from gpiozero import DigitalOutputDevice, PWMOutputDevice

            try:
                # Disable both channels before initializing direction outputs.
                self._ena = self._create(PWMOutputDevice, MOTOR_ENA)
                self._enb = self._create(PWMOutputDevice, MOTOR_ENB)
                self._in1 = self._create(DigitalOutputDevice, MOTOR_IN1)
                self._in2 = self._create(DigitalOutputDevice, MOTOR_IN2)
                self._in3 = self._create(DigitalOutputDevice, MOTOR_IN3)
                self._in4 = self._create(DigitalOutputDevice, MOTOR_IN4)
            except Exception:
                for device in reversed(self._devices):
                    device.close()
                raise

    def _create(self, device_class, pin):
        device = device_class(pin, initial_value=0)
        self._devices.append(device)
        return device

    def moveForward(self, speed):
        """Run both sides forward at speed percent."""
        self._move(speed, 1, 1)

    def moveBackward(self, speed):
        """Run both sides backward at speed percent."""
        self._move(speed, -1, -1)

    def turnRight(self, speed):
        """Spin right: left side forward, right side backward."""
        self._move(speed, 1, -1)

    def turnLeft(self, speed):
        """Spin left: left side backward, right side forward."""
        self._move(speed, -1, 1)

    def _move(self, speed, left, right):
        if self._closed:
            raise RuntimeError("MotorDriver is closed.")
        if (isinstance(speed, bool) or not isinstance(speed, (int, float))
                or not math.isfinite(speed) or not 0 <= speed <= 100):
            raise ValueError("Speed must be a finite number from 0 to 100 percent.")
        if speed == 0:
            self.stop()
            return
        if self.demo:
            print(f"[DEMO motors] left={left * speed}%, right={right * speed}%")
            return
        # Remove PWM before changing direction, then enable both channels.
        self.stop()
        self._in1.value = int(left > 0)
        self._in2.value = int(left < 0)
        self._in3.value = int(right > 0)
        self._in4.value = int(right < 0)
        self._ena.value = speed / 100
        self._enb.value = speed / 100

    def stop(self):
        """Disable both channels and clear direction outputs (coast)."""
        if self._closed:
            return
        if self.demo:
            print("[DEMO motors] stop")
        else:
            for device in self._devices:
                device.off()

    def close(self):
        """Stop the motors and release GPIO resources."""
        if self._closed:
            return
        try:
            self.stop()
        finally:
            for device in reversed(self._devices):
                device.close()
            self._closed = True
