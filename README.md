

# Buzzer project

`main.py` creates a `Buzzer` and passes it to `RoverController` in
`controller.py`. The LCD and motor modules have been removed.

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

`Description.txt` and `PROJECT_STATUS.md` describe the earlier rover scope
and are historical references, not the current implementation.
