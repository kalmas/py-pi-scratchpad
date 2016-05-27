import time
import RPi.GPIO as GPIO

pin = 16
pin2 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

p = GPIO.PWM(pin, 50)
p.start(0)

p2 = GPIO.PWM(pin2, 50)
p2.start(5)

##p2.ChangeDutyCycle(7.5)

try:
    while 1:
        for dc in range(50, 100, 2):
            dc_ratio = float(dc)/10
            p.ChangeDutyCycle(dc_ratio)
            p2.ChangeDutyCycle(dc_ratio)
            print dc_ratio
            time.sleep(1)
        for dc in range(100, 48, -2):
            dc_ratio = float(dc)/10
            p.ChangeDutyCycle(dc_ratio)
            p2.ChangeDutyCycle(dc_ratio)
            print dc_ratio
            time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
p2.stop()
GPIO.cleanup()

