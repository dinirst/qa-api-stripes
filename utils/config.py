import os

from dotenv import load_dotenv


load_dotenv()

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

if not STRIPE_SECRET_KEY:
    raise ValueError(
        "STRIPE_SECRET_KEY is not configured. "
        "Please set it in the .env file."
    )