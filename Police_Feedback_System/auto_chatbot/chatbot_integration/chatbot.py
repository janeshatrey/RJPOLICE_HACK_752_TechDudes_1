import dialogflow
import json
from google.oauth2 import service_account
from dialogflow_config import *

def detect_intent(user_text):
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(json.dumps(dialogflow_config))
    )

    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path("your_project_id", "unique_session_id")

    text_input = dialogflow.TextInput(text=user_text, language_code="en-US")
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text
