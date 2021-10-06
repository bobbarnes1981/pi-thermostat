
import json
import logging

from sensor import Sensor
from service import Service
from thinger import Thinger
from heater import Heater
from schedule import Schedule

config = {}
with open('config.json') as config_file:
    config = json.load(config_file)

logging.basicConfig(level=logging.DEBUG)

srv = Service(
    Sensor(config['inside']['serial'], config['inside']['temp_adj']),
    None,
    Heater(),
    Schedule(),
    Thinger(config['thinger']['user'], config['thinger']['bucket_id'], config['thinger']['auth_key']),
    config['delay_seconds']
)
#srv.daemon = True
srv.start()

