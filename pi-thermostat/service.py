
import logging
import time
from threading import Thread
from datetime import datetime

class Service(Thread):
    def __init__(self, sensor_inside, sensor_outside, heater, schedule, storage, delay_seconds):
        Thread.__init__(self)
        self.sensor_inside = sensor_inside
        self.sensor_outside = sensor_outside
        self.heater = heater
        self.schedule = schedule
        self.storage = storage
        self.delay_seconds = delay_seconds
        self.running = True
    def run(self):
        while self.running:
            logging.info("{0}".format(datetime.now()))
            outside_temperature = None
            if self.sensor_outside != None:
                outside_temperature = self.sensor_outside.temperature()
            current_temperature = self.sensor_inside.temperature()
            if current_temperature == None:
                logging.error("Could not get temperature")
                heating_state = False
            else:
                required_temperature = self.schedule.get_required_temperature()
                heating_state = current_temperature < required_temperature
            logging.info("Heating required: {0}".format(heating_state))
            self.heater.set_state(heating_state)
            self.storage.store(required_temperature, current_temperature, heating_state, outside_temperature)
            time.sleep(self.delay_seconds)

