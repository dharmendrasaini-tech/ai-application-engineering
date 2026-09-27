import requests
import logging

from .exceptions import ExternalServiceError

logger = logging.getLogger(__name__)


class ApiClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"
    TIMEOUT = 5

    def fetch_post(self, post_id: int) -> dict:

        api_url = f"{self.BASE_URL}/posts/{post_id}"


        try:

            response = requests.get(url=api_url, timeout=self.TIMEOUT)

            response.raise_for_status()

            data = response.json()

        except requests.RequestException as exc:
            logger.exception("Failed to fetch data from external service.")
            raise ExternalServiceError("Failed to fetch data from external service.") from exc

        if not isinstance(data, dict):
            logger.error("External service returned unexpected data.")
            raise ExternalServiceError("External service returned unexpected data.")


        required_fields = {
            "userId",
            "id",
            "title",
            "body",
        }

        if not required_fields.issubset(data.keys()):
            logger.error("External service returned incomplete data.")
            raise ExternalServiceError("External service returned incomplete data.")


        return data

