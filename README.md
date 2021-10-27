
# run #

python3 pi-thermostat

# auto #

/etc/rc.local

screen -m -d /usr/bin/python3 /home/pi/pi-thermostat/py-thermostat/ /home/pi/pi-thermostat/config.json

# requirements #

requests - python3-requests

RPi.GPIO - python3-rpi.gpio

