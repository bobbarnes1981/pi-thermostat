
class Heater(object):
    def __init__(self):
        self.heating = False
    def set_state(self, heating):
        print("Current heating state: {0}".format(self.heating))
        if heating != self.heating:
            self.heating = heating
            print("Change heating state to: {0}".format(heating))
        else:
            print("No change")


