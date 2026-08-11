from api.stripe_client import StripeClient


def test_invalid_api_key():
    client = StripeClient("sk_test_invalid")

    response = client.create_customer(
        name="Invalid Key Test",
        email="invalid-key@example.com",
    )

    assert response.status_code == 401

    data = response.json()

    assert "error" in data
    assert data["error"]["type"] == "invalid_request_error"