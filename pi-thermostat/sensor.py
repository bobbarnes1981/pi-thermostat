
import os

class Sensor(object):
    def __init__(self, temp_adj):
        self.path = self.get_path()
        self.temp_adj = temp_adj
    def get_path(self):
        BASE = '/sys/bus/w1/devices/'
        FILE = '/w1_slave'
        directories = os.listdir(BASE)
        for directory in directories:
            if directory.startswith('28'):
                return BASE + directory + FILE
        return None
    def raw(self):
        with open(self.path, 'r') as f:
            return f.readlines()
    def temperature(self):
        raw = self.raw()
        while raw[0].strip()[-3:] != 'YES':
            time.sleep(0.5)
            raw = self.raw()
        temp = float(raw[1].strip()[-5:]) / 1000 # convert to decimal
        temp = temp + self.temp_adj # adjust for rubbish sensors
        return temp

