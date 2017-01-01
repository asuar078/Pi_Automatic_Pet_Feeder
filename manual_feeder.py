import time
import RPi.GPIO as GPIO
import stepper

GPIO.setmode(GPIO.BCM)

button_pin = 18
led_pin = 17

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

led_state = False

def toggle_callback(channel):
    global led_state
    print "button pressed"
    led_state = not led_state

    stepper.turn_motor(150)

    if led_state == False:
        GPIO.output(led_pin, GPIO.LOW)
    elif led_state == True:
        GPIO.output(led_pin, GPIO.HIGH)

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=toggle_callback, bouncetime=300)

# GPIO.add_event_detect(buttonD, GPIO.RISING, pushMsg, bouncetime=50)

print "Waiting for button press"
try:
   while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
