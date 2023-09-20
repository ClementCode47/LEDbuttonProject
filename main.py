import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

try:
    while True:
        etat = GPIO.input(12)
        if etat == GPIO.HIGH:
            GPIO.output(14, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
        else:
            GPIO.output(14, GPIO.LOW)
            GPIO.output(15, GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.cleanup()