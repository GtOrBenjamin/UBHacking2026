# Rover project status

Report prepared from the conversation and a fresh workspace inspection.

## Current workspace

Location: `C:\Users\ngtha\OneDrive\Desktop\UBHacking`.

At inspection, the directory contained only `.git`. The previously created
Python modules, `Description.txt`, `requirements.txt`, and `README.md` were
not present. Their removal or relocation has not been investigated. This
report does not claim the earlier implementation is still available.

## Confirmed rover hardware

- Raspberry Pi 4; GPIO numbering uses BCM.
- Four wheels and four motors: two left, two right.
- One L298N module: channel A controls both left motors; channel B controls
  both right motors. Motors on each side share direction and PWM commands.
- ENA and ENB remain in use for PWM speed control.
- Piezo buzzer controlled using PWM; GPIO and electrical connections pending.
- LCD 1602 displaying `Detected`, `Clean`, and `Moving`; interface and wiring
  pending. LCD GPIO assignments should remain placeholders until confirmed.

| L298N signal | BCM GPIO | Physical Pi pin |
|---|---:|---:|
| IN1 | 17 | 11 |
| IN2 | 27 | 13 |
| IN3 | 22 | 15 |
| IN4 | 23 | 16 |
| ENA | 18 | 12 |
| ENB | 13 | 33 |

The intended wiring requires ENA/ENB jumpers removed for GPIO PWM control
and a common Pi/L298N ground. Actual wiring and motor direction have not
been tested. Motor models, supply specifications, and how each pair is
electrically connected remain unconfirmed.

An earlier description mentioned a RAM mechanism operated manually by a
switch and potentiometer. The user subsequently removed it from the latest
description, so it was excluded from the rewrite plan.

## Agreed software organization

| File | Responsibility |
|---|---|
| `main.py` | Construct devices, start the application, coordinate cleanup |
| `config.py` | GPIO assignments and device settings; does not operate pins |
| `motor_driver.py` | Motor direction, PWM speed, and stopping |
| `buzzer.py` | PWM tones and sound control |
| `lcd_display.py` | LCD initialization and status display |
| `controller.py` | Rover decisions and coordination between devices |

These six files were previously created as demo scaffolds. They printed
actions without accessing GPIO. Hardware backends and the operating algorithm
were explicitly unimplemented. The entry command was `python main.py --demo`.
They are currently absent from this workspace.

## Python and dependencies

The user chose to proceed without a virtual environment.

Requested dependency list:

```text
gpiozero
RPLCD
smbus2
```

The same unpinned list had previously been observed in `requirements.txt`.
The latest dependency-update request was interrupted; no subsequent dependency
installation or version update has been verified. The requirements file is
currently absent. The demo scaffolds used only the Python standard library;
hardware libraries were intended for later implementation. LCD dependencies
must be checked against the final interface and backend.

Earlier attempts to run `python` in this Windows terminal failed with
"The file cannot be accessed by the system". The command resolved to
`Microsoft\WindowsApps\python.exe`; `py` was not found. This does not prove
Python is uninstalled. No successful demo or hardware execution was verified.

## Pending work

1. Locate or restore the project files before continuing implementation.
2. Make a working Python interpreter available on the development machine
   or run the project on the Raspberry Pi.
3. Restore the requirements file and install/verify the hardware dependencies
   in the intended Raspberry Pi environment, without a venv as requested.
4. Confirm LCD interface (I2C or parallel), wiring, and any I2C address.
5. Confirm buzzer GPIO, model, electrical connection, and desired sound behavior.
6. Define command input, rover algorithm, and LCD state transitions.
7. Implement hardware backends and verify each device before integrated tests.

No camera, detection sensor, encoder, or distance sensor has been confirmed.
The label `Detected` alone does not establish what hardware performs detection.

## Report placement

This report is inside the project folder on the Desktop. The session permits
writes only inside this project workspace, so it was not saved directly in
the parent Desktop directory.
