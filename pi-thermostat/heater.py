
import logging
import RPi.GPIO as GPIO

class Heater(object):
    def __init__(self, pin):
        self.pin = pin
        self.heating = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, self.heating)
    def set_state(self, heating):
        logging.info("Current heating state: {0}".format(self.heating))
        if heating != self.heating:
            self.heating = heating
            logging.info("Change heating state to: {0}".format(self.heating))
        else:
            logging.info("No change")
        GPIO.output(self.pin, self.heating)
    def __del__(self):
        GPIO.cleanup()

