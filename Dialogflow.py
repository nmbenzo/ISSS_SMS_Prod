import os
import dialogflow_v2 as dialogflow
from auth_token import project_id, session_id


credentials_path = 'isss-chatbot-dev.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


class DialogFlow():
    """
    A class to authenticate and point to a specific Dialogflow Agent. This will
    allow for multiple agents to be selected based on user response without
    having to create multiple separate functions
    """
    def __init__(self, project_id, language_code, session_id):
        self.project_id = project_id
        self.language_code = language_code
        self.session_id = session_id

    def detect_intent_response(self, text):
        """Returns the result of detect intent with texts as inputs.
        Using the same `session_id` between requests allows continuation
        of the conversation."""

        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)

        text_input = dialogflow.types.TextInput(
            text=text, language_code=self.language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        return_text = response.query_result.fulfillment_text

        return str(return_text)


smart_message = DialogFlow(project_id, 'en=US', session_id)

