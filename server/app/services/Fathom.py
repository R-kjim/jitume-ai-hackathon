import requests

from server.app.config.config import variables


class FathomHandler():
    def __init__(self):
        self.api_key = variables.fathom_api_key

    def create_webhook(self):
        url = "https://api.fathom.ai/external/v1/webhooks"

        payload = {
            "destination_url": f"{variables.backend_url}/api/agents/fathom-webhook",
            "triggered_for": ["my_recordings"],
            "include_action_items": False,
            "include_crm_matches": False,
            "include_summary": True,
            "include_transcript": True
        }
        headers = {
            "X-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)

fathom_handler = FathomHandler()

