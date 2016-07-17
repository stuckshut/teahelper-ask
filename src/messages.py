from tea_info import tea_info

welcome = "What type of tea would you like to know about?"
steeping = "steep {0} for {1} at {2} degrees fahrenheit"
help_msg = "I can tell you about {0} tea"
error = "I'm sorry, I have encountered an error"


def get_welcome_response():
    return welcome


def get_steeping_response(tea_type, time, temp):
    return steeping.format(tea_type, time, temp)


def get_error_response():
    return error


def get_help_response():
    teas = []
    for tea, info in tea_info.iteritems():
        teas.append(tea)
    msg = ", ".join(teas)
    k = msg.rfind(',')
    msg = msg[:k] + ", or" + msg[k+1:]
    return msg
