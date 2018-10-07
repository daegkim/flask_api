import json


class vehicle_info:
    def __init__(self):
        self.number = ''

    def setNumber(self, num):
        self.number = num

    def toJSON(self):
        #lamda
        #indent
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
