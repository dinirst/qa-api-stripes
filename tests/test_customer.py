from jsonschema import validate

from schemas.customer_schema import customer_schema


def test_create_customer(stripe_client):
    response = stripe_client.create_customer(
        name="QA Automation Test",
        email="qa@example.com",
        description="Created by API automation",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["object"] == "customer"
    assert data["id"].startswith("cus_")
    assert data["email"] == "qa@example.com"
    assert data["name"] == "QA Automation Test"
    assert data["livemode"] is False

    # Schema validation
    validate(
        instance=data,
        schema=customer_schema,
    )

    # Performance check
    response_time = response.elapsed.total_seconds()

    print(f"Create customer response time: {response_time:.3f}s")

    assert response_time < 2.0, (
        f"API response took {response_time:.3f}s, "
        "which exceeds the 2-second threshold."
    )


def test_retrieve_customer(stripe_client):
    create_response = stripe_client.create_customer(
        name="QA Retrieve Test",
        email="qa.retrieve@example.com",
        description="Customer for retrieve test",
    )

    assert create_response.status_code == 200

    created_data = create_response.json()
    customer_id = created_data["id"]

    retrieve_response = stripe_client.get_customer(customer_id)

    assert retrieve_response.status_code == 200

    retrieved_data = retrieve_response.json()

    assert retrieved_data["object"] == "customer"
    assert retrieved_data["id"] == customer_id
    assert retrieved_data["email"] == "qa.retrieve@example.com"
    assert retrieved_data["name"] == "QA Retrieve Test"
    assert retrieved_data["livemode"] is False

    # Schema validation
    validate(
        instance=retrieved_data,
        schema=customer_schema,
    )

    # Performance check
    response_time = retrieve_response.elapsed.total_seconds()

    print(f"Retrieve customer response time: {response_time:.3f}s")

    assert response_time < 2.0, (
        f"API response took {response_time:.3f}s, "
        "which exceeds the 2-second threshold."
    )


def test_invalid_customer_id(stripe_client):
    response = stripe_client.get_customer("cus_invalid123")

    assert response.status_code == 404

    data = response.json()

    assert "error" in data