"""Payment gateway client.

This is a fake gateway for local development: card tokens starting with
``tok_declined`` are declined, everything else is approved.
"""
import uuid
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from .logger import get_logger

log = get_logger("payment")


@dataclass
class PaymentResult:
    success: bool
    amount: Decimal
    transaction_id: Optional[str] = None
    message: str = ""


class PaymentGateway:
    def charge(self, amount: Decimal, card_token: str) -> PaymentResult:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if card_token.startswith("tok_declined"):
            log.warning("Payment declined")
            return PaymentResult(success=False, amount=amount, message="Card declined")
        transaction_id = f"txn_{uuid.uuid4().hex[:12]}"
        log.info("Charged %s (%s)", amount, transaction_id)
        return PaymentResult(success=True, amount=amount, transaction_id=transaction_id, message="Approved")
