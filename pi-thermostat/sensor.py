
import logging
import os

class Sensor(object):
    BASE_PATH = '/sys/bus/w1/devices/'
    FILE_NAME = '/w1_slave'
    def __init__(self, serial, temp_adj):
        if serial == None:
            self.serial = self.get_serial()
        else:
            self.serial = serial
        self.path = self.BASE_PATH + self.serial + self.FILE_NAME
        self.temp_adj = temp_adj
        logging.info("Sensor serial: {0}".format(self.serial))
        logging.info("Sensor path: {0}".format(self.path))
    def get_serial(self):
        directories = os.listdir(self.BASE_PATH)
        for directory in directories:
            if directory.startswith('28'):
                return directory
        return None
    def raw(self):
        with open(self.path, 'r') as f:
            return f.readlines()
    def temperature(self):
        try:
            raw = self.raw()
            while raw[0].strip()[-3:] != 'YES':
                time.sleep(0.5)
                raw = self.raw()
            temp = float(raw[1].strip()[-5:]) / 1000 # convert to decimal
            logging.info("Measured: {0}".format(temp))
            temp = temp + self.temp_adj # adjust for rubbish sensors
            logging.info("Adjusted: {0}".format(temp))
            return temp
        except Exception as e:
            logging.error(e)
        return None
