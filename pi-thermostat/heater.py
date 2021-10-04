
import logging

class Heater(object):
    def __init__(self):
        self.heating = False
    def set_state(self, heating):
        logging.info("Current heating state: {0}".format(self.heating))
        if heating != self.heating:
            self.heating = heating
            logging.info("Change heating state to: {0}".format(self.heating))
        else:
            logging.info("No change")


