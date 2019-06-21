import os
import dialogflow_v2 as dialogflow


credentials_path = 'isss-chatbot-dev.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


def detect_intent_response(text):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    project_id = 'isss-chatbot-dev-iysogc'
    language_code = 'en=US'
    session_id = 'nbenzschawel'

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    return_text = response.query_result.fulfillment_text

    return str(return_text)

