"""Run a small end-to-end demo of the API from the command line.

    python -m src.app
"""
from . import config
from .auth import hash_password, login
from .checkout import Cart, calculate_total, checkout
from .payment import PaymentGateway
from .user import UserRepository


def main() -> int:
    print(f"{config.APP_NAME} {config.VERSION} ({config.ENVIRONMENT})")

    users = UserRepository()
    users.add("priya@shopeasy.example", "Priya", hash_password("correct-horse-42"))
    user = login(users, "priya@shopeasy.example", "correct-horse-42")
    print(f"Logged in as {user.name}")

    cart = Cart()
    cart.add("SKU-100", "Coffee beans", "12.50", quantity=2)
    cart.add("SKU-200", "French press", "29.00")
    summary = calculate_total(cart)
    print(f"Subtotal {summary.subtotal}  Shipping {summary.shipping}  Tax {summary.tax}  Total {summary.total} {config.CURRENCY}")

    result = checkout(cart, PaymentGateway(), "tok_visa")
    print(f"Payment: {result.message} ({result.transaction_id})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
