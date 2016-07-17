import messages
from tea_info import tea_info
from response import Response


def on_launch(request, session):
    return Response.create_ask_response(
        messages.get_welcome_response()
    )


def on_intent(request, session):
    if request.intent_name == 'GetTeaInfo':
        if 'TeaType' in request.slots and request.slots['TeaType'] in tea_info:
            tea_type = request.slots['TeaType']
            time = tea_info['tea_type']['time']
            temp = tea_info['tea_type']['temp']
            return Response.create_tell_response(
                messages.get_steeping_response(tea_type, time, temp)
            )

    # Other intents ...

    # If we drop through all the intents, we probably failed somehow
    return on_error(request, session)


def on_session_ended(request, session):
    pass


def on_error(request, session):
    return Response.create_tell_response(messages.get_error_response())
