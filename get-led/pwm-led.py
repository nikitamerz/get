import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)
#дьюти определяет, на сколько процентов включен светодиод
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1
    if duty > 100.0:
        duty = 0.0
