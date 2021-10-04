
class Schedule(object):
    def __init__(self):
        pass
    def needs_heating(self, temp):
        if temp < 20.0:
            return True
        return False

