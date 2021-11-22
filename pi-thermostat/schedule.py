
import logging
import sqlite3

from datetime import datetime

class Schedule(object):
    FROST_PROTECTION = 5
    def __init__(self, database):
        self.database = database
        self.db_create()
        if self.db_isempty():
            self.db_populate()    
    def db_create(self):
        try:
            con = sqlite3.connect(self.database)
            cur = con.cursor()
            qry = 'CREATE TABLE IF NOT EXISTS schedule (day INTEGER, hour INTEGER, temperature INTEGER, UNIQUE(day, hour));'
            cur.execute(qry)
            con.commit()
            con.close()
        except Exception as e:
            print(e)
    def db_isempty(self):
        rows = 0
        try:
            con = sqlite3.connect(self.database)
            cur = con.cursor()
            qry = 'SELECT COUNT(temperature) AS rows FROM schedule;'
            res = cur.execute(qry).fetchone()
            rows = res[0]
            con.close()
        except Exception as e:
            print(e)
        return rows == 0
    def db_populate(self):
        try:
            con = sqlite3.connect(self.database)
            cur = con.cursor()
            qry = 'INSERT INTO schedule (day, hour, temperature) VALUES (?, ?, ?)'
            default_temperature = self.FROST_PROTECTION
            for day in range(0, 7):
                for hour in range(0, 24):
                    cur.execute(qry, (day, hour, default_temperature))
            con.commit()
            con.close()
        except Exception as e:
            print(e)
    def get_required_temperature(self):
        t = datetime.now()
        required_temperature = 0
        try:
            con = sqlite3.connect(self.database)
            cur = con.cursor()
            qry = 'SELECT temperature FROM schedule WHERE day = ? AND hour = ?'
            res = cur.execute(qry, (t.weekday(), t.hour)).fetchone()
            required_temperature = res[0]
            con.close()
        except Exception as e:
            print(e)
        if required_temperature < self.FROST_PROTECTION:
            logging.info("Frost protection: {0}".format(self.FROST_PROTECTION))
        logging.info("Day: {0}".format(t.weekday()))
        logging.info("Hour: {0}".format(t.hour))
        logging.info("Required: {0}".format(required_temperature))
        return required_temperature

