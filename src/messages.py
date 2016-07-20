from tea_info import tea_info

welcome = "What type of tea would you like to know about?"
steeping = "steep {0} tea for {1} at {2} degrees fahrenheit."
help_msg = "I can tell you about {0} tea."
error = "I'm sorry, I have encountered an error, try again."
prompt_msg = "Which tea would you like to know about?"
end_session = "Goodbye."


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
    teas[-1] = 'or ' + teas[-1]
    teas_str = ", ".join(teas)
    return help_msg.format(teas_str)


def get_prompt_response():
    return prompt_msg


def get_end_response():
    return end_session
