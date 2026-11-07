"""LCD 1602 status display interface."""

from config import LCD_STATES


class LCDDisplay:
    """Demo implementation until LCD interface and wiring are confirmed."""

    def __init__(self, *, demo=True):
        if not demo:
            raise NotImplementedError("Confirm LCD interface and wiring before implementation.")
        self.status = None

    def show_status(self, status):
        if status not in LCD_STATES:
            raise ValueError(f"Status must be one of {LCD_STATES}.")
        if status != self.status:
            self.status = status
            print(f"[DEMO LCD] {status}")

    def clear(self):
        self.status = None
        print("[DEMO LCD] clear")

    def close(self):
        self.clear()
