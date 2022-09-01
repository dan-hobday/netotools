import requests
from dataclasses import dataclass


@dataclass
class NetoAPICall:
    endpoint: str
    params: dict
    headers: dict


class NetoAPIClient:
    """Neto API client for handling API calls"""

    def __init__(
        self, base_url: str, api_endpoint: str, username: str, api_key: str
    ) -> None:
        self.base_url = base_url
        self.api_endpoint = api_endpoint
        self.username = username
        self.api_key = api_key
        self.apicall = None
        self.session = requests.session()

    def set_api_call(self, action: str, request_params: dict) -> None:
        """Define an api call object"""
        data = {
            "endpoint": f"{self.base_url}{self.api_endpoint}",
            "params": request_params,
            "headers": {
                "USERNAME": self.username,
                "API_KEY": self.api_key,
                "ACTION": action,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        }
        self.apicall = NetoAPICall(**data)

    def execute_api_call(self) -> dict:
        """Execute an api call and return the response"""
        json_response = self.session.post(
            self.apicall.endpoint,
            json=self.apicall.params,
            headers=self.apicall.headers,
        )
        if json_response.status_code != 200:
            raise ConnectionError(
                f"Request failed with status_code {json_response.status_code}"
            )
        response = json_response.json()
        if response["Ack"] == "Error":
            raise ValueError(response["Messages"])

        return response
