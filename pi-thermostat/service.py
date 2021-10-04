
import time
from threading import Thread
from datetime import datetime

class Service(Thread):
    def __init__(self, sensor, heater, schedule, storage):
        Thread.__init__(self)
        self.sensor = sensor
        self.heater = heater
        self.schedule = schedule
        self.storage = storage
        self.running = True
    def run(self):
        while self.running:
            temp = self.sensor.temperature()
            print("{0}".format(datetime.now()))
            print("Measured: {0}".format(temp))
            if self.schedule.needs_heating(temp):
                self.heater.set_state(True)
            else:
                self.heater.set_state(False)
            self.storage.store(temp)
            time.sleep(60)

