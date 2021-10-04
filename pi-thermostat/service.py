
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
            current_temperature = self.sensor.temperature()
            print("{0}".format(datetime.now()))
            print("Measured: {0}".format(current_temperature))
            required_temperature = self.schedule.get_required_temperature()
            heating_state = current_temperature < required_temperature
            self.heater.set_state(heating_state)
            self.storage.store(required_temperature, current_temperature, heating_state)
            time.sleep(60)

