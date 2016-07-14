from __future__ import print_function

import json

tea_times = {
        "white": {
            "time": "2 to 3 minutes",
            "temp": "170 degrees fahrenheit"
            },
        "green": {
            "time": "2 to 3 minutes",
            "temp": "175 degress fahrenheit"
            }
        "oolong": {
            "time": "2 to 5 minutes",
            "temp": "185 degrees fahrenheit"
            }
        "black": {
            "time": "3 to 5  minutes",
            "temp": "208 degrees fahrenheit"
            }
        "pu-erh": {
            "time": "2 to 3 minutes",
            "temp": "208 degrees fahrenheit"
            }
        "herbal": {
            "time": "4 to 6 minutes",
            "temp": "212 degrees fahrenheit"
            }
        }


def lambda_handler(event, context):
    print("tea type = " + event['type'])

