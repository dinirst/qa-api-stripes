# Stripe API Automation

API automation project using Python, Requests, and Pytest for testing the Stripe Test API.

## Project Overview

This project demonstrates API automation practices including:

- Positive API flows
- Negative API flows
- API authentication handling
- Response data validation
- JSON Schema validation
- API response time validation
- Environment-based secret management
- Pytest fixtures
- HTML test reporting
- GitHub Actions CI

## Tech Stack

- Python 3.12
- Pytest
- Requests
- python-dotenv
- jsonschema
- pytest-html
- GitHub Actions

## Project Structure

```text
QA-API-STRIPES/
│
├── api/
│   └── stripe_client.py
│
├── schemas/
│   └── customer_schema.py
│
├── tests/
│   ├── test_authentication.py
│   └── test_customer.py
│
├── utils/
│   └── config.py
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
├── conftest.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md