"""Application settings for shop-easy-api.

Values can be overridden with environment variables so the same code runs in
development, staging and production.
"""
import os
from decimal import Decimal

APP_NAME = "shop-easy-api"
VERSION = "2.3.1"
ENVIRONMENT = os.environ.get("SHOPEASY_ENV", "development")
BASE_URL = os.environ.get("SHOPEASY_BASE_URL", "http://localhost:8000")
SUPPORT_EMAIL = "support@shopeasy.example"

CURRENCY = "USD"
TAX_RATE = Decimal("0.08")
SHIPPING_FEE = Decimal("4.99")
FREE_SHIPPING_THRESHOLD = Decimal("50.00")

# Feature flags let us deploy code with a feature switched off.
FEATURE_FLAGS = {}
MAX_RESULTS = 10

def is_enabled(flag: str) -> bool:
    env = os.environ.get(f"SHOPEASY_FF_{flag.upper()}")
    if env is not None:
        return env.lower() in ("1", "on", "true")
    return FEATURE_FLAGS.get(flag, False)
