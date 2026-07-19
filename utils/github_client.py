import time
import requests

from config.settings import (
    GITHUB_API_URL,
    GITHUB_TOKEN,
    REQUEST_DELAY
)


class GitHubClient:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "Accept": "application/vnd.github+json",

            "Authorization": f"Bearer {GITHUB_TOKEN}",

            "X-GitHub-Api-Version": "2022-11-28"

        })

    def get(self, endpoint, params=None):

        response = self.session.get(
            f"{GITHUB_API_URL}{endpoint}",
            params=params
        )

        response.raise_for_status()

        time.sleep(REQUEST_DELAY)

        return response.json(), response.headers