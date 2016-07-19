import messages
from tea_info import tea_info
from response import Response


def on_launch(request, session):
    return Response.create_ask_response(
        messages.get_welcome_response()
    )


def on_intent(request, session):
    if request.intent_name == 'GetTeaInfo':
        if 'TeaType' in request.slots.keys():
            if request.slots['TeaType'].get('value') in tea_info.keys():
                tea_type = request.slots['TeaType']['value']
                time = tea_info[tea_type]['time']
                temp = tea_info[tea_type]['temp']
                return Response.create_tell_response(
                    messages.get_steeping_response(tea_type, time, temp)
                )
            else:
                return Response.create_ask_response(
                    messages.get_help_response()
                )
    elif request.intent_name == 'AMAZON.HelpIntent':
        return Response.create_ask_response(
            messages.get_help_response()
        )

    elif request.intent_name == 'AMAZON.StopIntent' or request.intent_name == 'AMAZON.CancelIntent':
        return Response.create_tell_response(
            messages.get_end_response()
        )

    # If we drop through all the intents, we probably failed somehow
    return on_error(request, session)


def on_session_ended(request, session):
    return Response.create_tell_response("")


def on_error(request, session):
    return Response.create_tell_response(messages.get_error_response())
