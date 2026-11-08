

# Rover project

`main.py` creates a `Buzzer` and `MotorDriver` and passes them to
`RoverController` in `controller.py`. Motor commands are available through
the controller; the current run routine still only plays the melody.

`MotorDriver` provides `moveForward(speed)`, `moveBackward(speed)`,
`turnRight(speed)`, and `turnLeft(speed)`. Speed is 0–100 percent; 0 stops.
Turns spin in place. Commands continue until another command or `stop()`.
`close()` stops the motors and releases GPIO; `main.py` handles cleanup.
For example, future controller logic can call `self.moveForward(40)` and
later `self.stop()`. No movement sequence or OpenCV behavior is configured.

Motor pins use BCM numbering: IN1=17, IN2=27 (left), IN3=22, IN4=23
(right), ENA=18 and ENB=13 (PWM). Remove ENA/ENB jumpers and connect
Pi/L298N grounds as described in `Description.txt`. Actual forward direction
depends on motor wiring and has not been verified on hardware.

Run the simulated melody:

```sh
python3 main.py --demo
```

The demo prints actions and waits for each note without accessing GPIO or
requiring gpiozero. On the Raspberry Pi, with gpiozero installed, run
`python3 main.py` to play the same melody on a passive PWM piezo buzzer.
`BUZZER_PIN` in `config.py` defaults to BCM 12, as listed in `Description.txt`;
set it to match your wiring.

Call `buzzer.playingSound([(440, 0.5), (0, 0.2), (523, 0.5)])` with a list of
`(frequency in Hz, duration in seconds)` pairs. Frequency 0 creates a rest.
Values must be finite nonnegative numbers; zero-duration notes are skipped.
Playback blocks until the melody finishes and turns the buzzer off even if
interrupted. Demo playback prints to the terminal; it does not produce audio
through the computer speakers. Edit the example melody in `controller.py`.

`Description.txt` supplies the motor wiring. `PROJECT_STATUS.md` is a
historical report and does not describe the current implementation.
