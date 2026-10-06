from decimal import Decimal

import pytest

from src.checkout import Cart, calculate_total, checkout
from src.payment import PaymentGateway


def test_small_order_pays_shipping_and_tax():
    cart = Cart()
    cart.add("SKU-100", "Coffee beans", "12.50", quantity=2)
    summary = calculate_total(cart)
    assert summary.subtotal == Decimal("25.00")
    assert summary.shipping == Decimal("4.99")
    assert summary.tax == Decimal("2.00")
    assert summary.total == Decimal("31.99")


def test_large_order_ships_free():
    cart = Cart()
    cart.add("SKU-300", "Espresso machine", "199.00")
    assert calculate_total(cart).shipping == Decimal("0.00")


def test_empty_cart_cannot_check_out():
    with pytest.raises(ValueError):
        checkout(Cart(), PaymentGateway(), "tok_visa")


def test_checkout_charges_the_total():
    cart = Cart()
    cart.add("SKU-200", "French press", "29.00")
    result = checkout(cart, PaymentGateway(), "tok_visa")
    assert result.success
    assert result.amount == calculate_total(cart).total
