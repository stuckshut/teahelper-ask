"""
Build a response object to send back to Alexa
"""


class Response:

    def __init__(self):
        self.version = '1.0'
        self.sessionAttributes = None
        self.shouldEndSession = True
        self.outputSpeech = {
            'type': 'string',
            'text': 'Default Response'
        }
        self.card = {
            "type": "string",
            "title": "string",
            "content": "string",
            "text": "string",
            "image": {
                "smallImageUrl": "string",
                "largeImageUrl": "string"
            }
        }

    def create_tell_response(self, message):
        self.shouldEndSession = True
        pass

    def create_ask_response(self, message):
        self.shouldEndSession = False
        pass