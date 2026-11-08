

# Rover project

Print ultrasonic distance readings on the Pi every approximately 0.5 seconds:

```sh
python3 distantsensor.py
# Or through RoverController (also initializes the LCD and buzzer):
python3 main.py
```

Add `--demo` to either command for simulated 100 cm readings without GPIO.
Press Ctrl+C to stop and release the sensor pins. `distantSensor.readDistance()`
returns centimeters, or `None` for a missing/stuck echo. Python pulse timing
is approximate and may be affected by Linux scheduling. Space direct reads
at least 60 ms apart. The current description specifies Trigger BCM 19 and
Echo BCM 26. Standard HC-SR04 Echo signals require a voltage divider or level
shifter before the Pi input. The description's model spelling is `HCFR04`;
the implementation follows the HC-SR04-style trigger/echo interface indicated
by the existing scaffold.

The controller constructs its distance sensor and reports readings during
normal startup. Its existing melody is available through `playMelody()`;
it does not play automatically during continuous distance reporting.

`main.py` creates a `Buzzer` and `lcdDisplay` and passes them to
`RoverController` in `controller.py`. The controller shows LCD messages while
playing the melody. Motor code is retained but temporarily disconnected.

`MotorDriver` provides `moveForward(speed)`, `moveBackward(speed)`,
`turnRight(speed)`, and `turnLeft(speed)`. Speed is 0–100 percent; 0 stops.
Turns spin in place. Commands continue until another command or `stop()`.
`close()` stops the motors and releases GPIO. Future controller logic can
call a connected driver's `moveForward(40)` and later `stop()`.
No movement sequence or OpenCV behavior is configured.

Motor pins use BCM numbering: IN1=17, IN2=27 (left), IN3=22, IN4=23
(right), ENA=18 and ENB=13 (PWM). Remove ENA/ENB jumpers and connect
Pi/L298N grounds as described in `Description.txt`. Actual forward direction
depends on motor wiring and has not been verified on hardware.

Run the simulated melody:

```sh
python3 main.py --demo
```

The demo prints actions and waits for each note without accessing GPIO or
requiring hardware libraries. On the Raspberry Pi, install requirements and run
`python3 main.py` to play the same melody on a passive PWM piezo buzzer.
`BUZZER_PIN` in `config.py` defaults to BCM 12, as listed in `Description.txt`;
set it to match your wiring.

LCD1602 setup:
- Enable I2C on the Raspberry Pi and connect SDA1 (BCM 2, physical pin 3)
  and SCL1 (BCM 3, physical pin 5).
- Set `LCD_I2C_ADDRESS` and `LCD_I2C_EXPANDER` in `config.py` to match your
  backpack. They are deliberately unset until confirmed. An I2C scan with
  `i2cdetect -y 1` reports addresses; inspect the chip marking for its type.
- Install dependencies with `python3 -m pip install -r requirements.txt`.
- Run `python3 main.py --demo` for logs, or `python3 main.py` for hardware.

Call the LCD methods from `controller.py` using:

```python
self.lcd.writeFirstLine("Detected")
self.lcd.writeSecondLine("Moving")
self.lcd.clearFirstLine()
self.lcd.clearSecondLine()
self.lcd.clearAll()
```

Each write replaces that row, truncates text to 16 characters, and pads
shorter text with spaces. Text must be printable ASCII without newlines.
`main.py` clears the display, turns off its backlight, and closes the bus
on exit. Hardware configuration errors are reported rather than silently
switching to demo mode.

Call `buzzer.playingSound([(440, 0.5), (0, 0.2), (523, 0.5)])` with a list of
`(frequency in Hz, duration in seconds)` pairs. Frequency 0 creates a rest.
Values must be finite nonnegative numbers; zero-duration notes are skipped.
Playback blocks until the melody finishes and turns the buzzer off even if
interrupted. Demo playback prints to the terminal; it does not produce audio
through the computer speakers. Edit the example melody in `controller.py`.

`Description.txt` supplies the motor wiring. `PROJECT_STATUS.md` is a
historical report and does not describe the current implementation.
