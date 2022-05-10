from escpos.printer import Serial
import os


class PrinterManager:
    line_width = 32
    border = "#" * 32

    def __init__(self) -> None:
        # """ 9600 Baud, 8N1, Flow Control Enabled """
        self.p = Serial(devfile='/dev/serial0',
                        baudrate=9600,
                        bytesize=8,
                        parity='N',
                        stopbits=1,
                        timeout=1.00,
                        dsrdtr=True)

        pass

    def print(self, str):
        self.p.text(str)
        self.p.cut()
