import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0.0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        self.pwm.ChangeDutyCycle(int(voltage/self.dynamic_range*100))
if __name__ == 'main':
    dac = PWM_DAC(12, 500, 3.290, True)
    try:
        while True:
            try:
                voltage = float(input('Enter voltage: '))
                dac.set_voltage(voltage)
            except ValueError as mtg:
                print(f"(mtg)\n Not number. Try again\n")

    finally:
        dac.deinit()