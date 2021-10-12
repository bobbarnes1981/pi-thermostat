
import logging

from datetime import datetime

class Schedule(object):
    def __init__(self, data):
        self.data = {}
        for d in data.keys():
            self.data[int(d)] = data[d]
    def get_required_temperature(self):
        t = datetime.now().time()
        required_temperature = self.data[t.hour]
        logging.info("Hour: {0}".format(t.hour))
        logging.info("Required: {0}".format(required_temperature))
        return required_temperature

