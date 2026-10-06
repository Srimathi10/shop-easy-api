from decimal import Decimal

import pytest

from src.payment import PaymentGateway


def test_approved_payment_has_transaction_id():
    result = PaymentGateway().charge(Decimal("10.00"), "tok_visa")
    assert result.success and result.transaction_id.startswith("txn_")


def test_declined_card():
    result = PaymentGateway().charge(Decimal("10.00"), "tok_declined_insufficient_funds")
    assert not result.success


def test_amount_must_be_positive():
    with pytest.raises(ValueError):
        PaymentGateway().charge(Decimal("0"), "tok_visa")
