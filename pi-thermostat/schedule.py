
import logging

from datetime import datetime

class Schedule(object):
    def __init__(self):
        self.data = {
            0: 15.0,
            1: 15.0,
            2: 15.0,
            3: 15.0,
            4: 15.0,
            5: 15.0,
            6: 20.0,
            7: 20.0,
            8: 20.0,
            9: 20.0,
            10: 20.0,
            11: 20.0,
            12: 20.0,
            13: 20.0,
            14: 20.0,
            15: 20.0,
            16: 20.0,
            17: 20.0,
            18: 15.0,
            19: 15.0,
            20: 15.0,
            21: 15.0,
            22: 15.0,
            23: 15.0,
        }
    def get_required_temperature(self):
        t = datetime.now().time()
        required_temperature = self.data[t.hour]
        logging.info("Required: {0}".format(required_temperature))
        return required_temperature

