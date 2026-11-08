"""Hardware configuration. All GPIO numbers use BCM numbering."""

# Buzzer GPIO listed in Description.txt; BCM numbering,
#GPIO 12, physics 32
BUZZER_PIN = 12

# L298N connections from Description.txt (BCM numbering).
MOTOR_IN1 = 17
MOTOR_IN2 = 27
MOTOR_IN3 = 22
MOTOR_IN4 = 23
MOTOR_ENA = 18
MOTOR_ENB = 13

# Distance sensor connections from Description.txt (BCM numbering).
DISTANCE_TRIGGER_PIN = 19
DISTANCE_ECHO_PIN = 26

# LCD1602 on I2C bus 1. Pins are managed by the I2C interface.
LCD_SDA_PIN = 2  # SDA1, physical pin 3
LCD_SCL_PIN = 3  # SCL1, physical pin 5
LCD_I2C_BUS = 1
LCD_I2C_ADDRESS = 0x27  # Address detected by the user's I2C scan.
LCD_I2C_EXPANDER = "PCF8574"  # PCF8574T backpack confirmed by the user.
