class Request:

    def __init__(self, request):
        self.type = request['type']
        self.timestamp = request['timestamp']
        self.requestId = request['requestId']

        if self.type == 'IntentRequest':
            self.intent_name = request['intent']['name']
            self.slots = request['intent']['slots']
        elif self.type == 'SessionEndedRequest':
            self.reason = request['reason']


class Session:

    def __init__(self, session):
        self.new = session['new']
        self.sessionId = session['sessionId']
        self.applicationId = session['application']['applicationId']
        self.attributes = session['attributes']
        self.userId = session['user']['userId']
