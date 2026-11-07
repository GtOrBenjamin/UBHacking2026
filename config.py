"""Hardware configuration. All GPIO numbers use BCM numbering."""

MOTOR_PINS = {
    "left_in1": 17,
    "left_in2": 27,
    "left_enable": 18,
    "right_in3": 22,
    "right_in4": 23,
    "right_enable": 13,
}
MOTOR_PWM_FREQUENCY = 1000
LEFT_INVERTED = False
RIGHT_INVERTED = False

# None means unassigned; choose unused GPIOs once wiring is confirmed.
BUZZER_PIN = None
LCD_INTERFACE = None  # Confirm I2C or parallel before implementing hardware.
LCD_PINS = {"rs": None, "enable": None, "d4": None,
            "d5": None, "d6": None, "d7": None}
LCD_I2C_ADDRESS = None
LCD_COLUMNS = 16
LCD_ROWS = 2
LCD_STATES = ("Detected", "Clean", "Moving")
