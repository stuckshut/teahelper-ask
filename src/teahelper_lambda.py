from __future__ import print_function

import json

from response import Response

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

    session = Session(event['session'])
    request = Request(event['request'])

    type = event['request']['intent']['slots']['TeaType']['value']
    print("tea type = " + type)
    time = tea_times[type]['time']
    temp = tea_times[type]['temp']

    message = time + ' at ' + temp
    return create_response(message=message)



class Request:

    def __init__(self, request):
        self.type = request['type']
        self.timestamp = request['timestamp']
        self.requestId = request['requestId']

        if self.type is 'IntentRequest':
            self.intent_name = request['intent']['name']
            self.slots = request['intent']['slots']
        elif self.type is 'SessionEndedRequest':
            self.reason = request['reason']


class Session:

    def __init__(self, session):
        self.new = session['new']
        self.sessionId = session['sessionId']
        self.applicationId = session['application']['applicationId']
        self.attributes = session['attributes']
        self.userId = session['user']['userId']
        self.accessToken = session['user']['accessToken']

