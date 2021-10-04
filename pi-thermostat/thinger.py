
import requests
import json

class Thinger(object):
    uriformat = "https://api.thinger.io/v1/users/{user}/buckets/{bucket_id}/data?authorization={auth_key}"
    def __init__(self, user, bucket_id, auth_key):
        self.rest_uri = self.uriformat.format(user=user, bucket_id=bucket_id, auth_key=auth_key)
    def store(self, required_temp, current_temp, heating_state):
        try:
            #print(self.rest_uri)
            print("Stored: {0} {1} {2}".format(required_temp, current_temp, heating_state))
            payload = {
                'required_temperature_c' : required_temp,
                'current_temperature_c' : current_temp,
                'heating_state' : heating_state
            }
            header = { 'content-type': 'application/json' }
            response = requests.post(self.rest_uri, data=json.dumps(payload), headers=header)
            print(response.status_code)
            print(response.text)
        except Exception as e:
            print(e)

