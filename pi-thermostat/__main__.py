
import json

from sensor import Sensor
from service import Service
from thinger import Thinger
from heater import Heater
from schedule import Schedule

config = {}
with open('config.json') as config_file:
    config = json.load(config_file)

srv = Service(Sensor(config['temp_adj']), Heater(), Schedule(), Thinger(config['thinger']['user'], config['thinger']['bucket_id'], config['thinger']['auth_key']))
#srv.daemon = True
srv.start()

