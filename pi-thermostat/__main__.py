
import json
import logging
import sys

from sensor import Sensor
from service import Service
from thinger import Thinger
from heater import Heater
from schedule import Schedule

config_path = 'config.json'
if len(sys.argv) == 2:
    config_path = sys.argv[1]
print("Config: {0}".format(config_path))

config = {}
with open(config_path) as config_file:
    config = json.load(config_file)

logging.basicConfig(level=logging.DEBUG)

srv = Service(
    Sensor(config['inside']['serial'], config['inside']['temp_adj']),
    Sensor(config['outside']['serial'], config['outside']['temp_adj']),
    Heater(config['heater']['pin']),
    Schedule(config['schedule']['database']),
    Thinger(config['thinger']['user'], config['thinger']['bucket_id'], config['thinger']['auth_key']),
    config['delay_seconds']
)
#srv.daemon = True
srv.start()

