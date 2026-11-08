
"""LCD1602 line operations with matching demo logs and I2C output."""

from config import LCD_I2C_ADDRESS, LCD_I2C_BUS, LCD_I2C_EXPANDER


class lcdDisplay:

    def __init__(self, *, demo=True, address=LCD_I2C_ADDRESS,
                 expander=LCD_I2C_EXPANDER, bus=LCD_I2C_BUS):
        self.demo = demo
        self._device = None
        self._closed = False
        if demo:
            print(f"[DEMO LCD] initialize 16x2 on I2C bus {bus}; backlight on")
        else:
            from RPLCD.i2c import CharLCD

            self._device = CharLCD(
                i2c_expander=expander, address=address, port=bus,
                cols=16, rows=2, auto_linebreaks=False,
                backlight_enabled=True,
            )
        try:
            self.clearAll()
        except Exception:
            self.close()
            raise

    def _check_open(self):
        if self._closed:
            raise RuntimeError("LCD display is closed.")

    def _write_line(self, row, text):
        self._check_open()
        if not isinstance(text, str):
            raise TypeError("LCD text must be a string.")
        if any(not 32 <= ord(char) <= 126 for char in text):
            raise ValueError("LCD text must contain only printable ASCII characters.")
        rendered = text[:16].ljust(16)
        if self.demo:
            print(f"[DEMO LCD] write line {row + 1}: |{rendered}|")
        else:
            self._device.cursor_pos = (row, 0)
            self._device.write_string(rendered)

    def writeFirstLine(self, text):
        """Replace the first row, truncating text to 16 characters."""
        self._write_line(0, text)

    def writeSecondLine(self, text):
        """Replace the second row, truncating text to 16 characters."""
        self._write_line(1, text)

    def clearFirstLine(self):
        """Erase only the first row."""
        self._write_line(0, "")

    def clearSecondLine(self):
        """Erase only the second row."""
        self._write_line(1, "")

    def clearAll(self):
        """Erase both rows."""
        self._check_open()
        if self.demo:
            print("[DEMO LCD] clear both lines")
        else:
            self._device.clear()

    def close(self):
        """Clear the display, switch off the backlight, and close the bus."""
        if self._closed:
            return
        try:
            if self.demo:
                print("[DEMO LCD] clear both lines; backlight off; close")
            else:
                try:
                    self._device.clear()
                    self._device.backlight_enabled = False
                finally:
                    try:
                        self._device.close()
                    finally:
                        self._device.bus.close()
        finally:
            self._closed = True
