from flask import Flask, request
import RPi.GPIO as GPIO
import time
import threading

app = Flask(__name__)
app.debug = True

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(11, GPIO.OUT) ## Setup GPIO Pin 0, PIN 11 to OUT
keep_blinking = False

def blink_it():
    GPIO.output(11, True)
    time.sleep(1)
    GPIO.output(11, False)
    time.sleep(1)
    print keep_blinking
    if (keep_blinking):
        t2 = threading.Thread(target=blink_it)
        t2.start()

@app.route("/on")
def on():
    GPIO.output(11, True)
    return "Is on."

@app.route("/off")
def off():
    GPIO.output(11, False)
    return "Is off."

@app.route("/blink-on")
def blink_on():
    global keep_blinking
    keep_blinking = True
    t = threading.Thread(target=blink_it)
    t.start()
    return 'ok'

@app.route("/blink-off")
def blink_off():
    global keep_blinking
    keep_blinking = False
    return 'ok'   

if __name__ == "__main__":
    app.run()
