from __future__ import print_function

import json

RAW_RESPONSE = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "PlainText",
            "text": "Some default text goes here."
                },
        "shouldEndSession": False
    }
}

tea_times = {
    "white": {
        "time": "2 to 3 minutes",
        "temp": "170 degrees fahrenheit"
    },
    "green": {
        "time": "2 to 3 minutes",
        "temp": "175 degrees fahrenheit"
    },
    "oolong": {
        "time": "2 to 5 minutes",
        "temp": "185 degrees fahrenheit"
    },
    "black": {
        "time": "3 to 5  minutes",
        "temp": "208 degrees fahrenheit"
    },
    "pu-erh": {
        "time": "2 to 3 minutes",
        "temp": "208 degrees fahrenheit"
    },
    "herbal": {
        "time": "4 to 6 minutes",
        "temp": "212 degrees fahrenheit"
    }
}


def lambda_handler(event, context):
    type = event['request']['intent']['slots']['TeaType']['value']
    print("tea type = " + type)
    time = tea_times[type]['time']
    temp = tea_times[type]['temp']

    message = time + ' at ' + temp
    return create_response(message=message)


def create_response(message=None, end_session=True):
    response = RAW_RESPONSE

    if message:
        response['response'] = {
            'outputSpeech': {
                'type': 'PlainText',
                'text': message
            }
        }
    response['response']['shouldEndSession'] = end_session
    return response
