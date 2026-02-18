import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False) -> None:
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self) -> None:
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number) -> None:
        if (0 <= number <= 255):
            binary = [int(el) for el in bin(number)[2:].zfill(8)]
            GPIO.output(self.gpio_bits, binary)
        else:
            GPIO.output(self.gpio_bits, 0)


    def set_voltage(self, voltage) -> None:

        userin = voltage

        def voltage_to_number(voltage) -> int:
            if not (0.0 <= voltage <= self.dynamic_range):
                print(f'Voltage out of DAC range (0.00 - {self.dynamic_range:.2f} V)')
                print('Setting 0 Volts')
                return 0
            return int(voltage / self.dynamic_range * 255)

        binary = [int(el) for el in bin(voltage_to_number(userin))[2:].zfill(8)]
        GPIO.output(self.gpio_bits, binary)

if __name__ == '__main__':
    try:
        dac = R2R_DAC([22, 27, 17, 26, 25, 21, 20, 16][::-1], 3.13, True)

        while True:
            try:
                voltage = float(input('Enter voltage: '))
                dac.set_voltage(voltage)

            except ValueError:
                print('Invalid input. Try again.\n')

    finally:
        dac.deinit()