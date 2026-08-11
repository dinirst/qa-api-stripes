import requests


class StripeClient:
    BASE_URL = "https://api.stripe.com/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}"
        }

    def create_customer(self, name, email, description=None):
        data = {
            "name": name,
            "email": email,
        }

        if description:
            data["description"] = description

        return requests.post(
            f"{self.BASE_URL}/customers",
            headers=self.headers,
            data=data,
        )

    def get_customer(self, customer_id):
        return requests.get(
            f"{self.BASE_URL}/customers/{customer_id}",
            headers=self.headers,
        )