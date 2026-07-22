import requests

from app.config.config import variables


class FathomHandler():
    def __init__(self):
        self.api_key = variables.fathom_api_key

    async def create_webhook(self):
        url = "https://api.fathom.ai/external/v1/webhooks"

        payload = {
            "destination_url": "https://example.com/webhook",
            "triggered_for": ["my_recordings", "my_shared_with_team_recordings", "shared_external_recordings"],
            "include_action_items": False,
            "include_crm_matches": False,
            "include_summary": False,
            "include_transcript": False
        }
        headers = {
            "X-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)