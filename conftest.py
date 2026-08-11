import pytest

from api.stripe_client import StripeClient
from utils.config import STRIPE_SECRET_KEY


@pytest.fixture
def stripe_client():
    return StripeClient(STRIPE_SECRET_KEY)