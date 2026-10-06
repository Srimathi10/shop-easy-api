"""Shopping cart and checkout."""
from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal
from typing import List

from . import config
from .payment import PaymentGateway, PaymentResult


def _money(value: Decimal) -> Decimal:
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass
class CartItem:
    sku: str
    name: str
    unit_price: Decimal
    quantity: int = 1

    @property
    def line_total(self) -> Decimal:
        return _money(self.unit_price * self.quantity)


@dataclass
class Cart:
    items: List[CartItem] = field(default_factory=list)

    def add(self, sku: str, name: str, unit_price: str, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        self.items.append(CartItem(sku, name, Decimal(unit_price), quantity))

    @property
    def subtotal(self) -> Decimal:
        return _money(sum((item.line_total for item in self.items), Decimal("0")))


@dataclass
class OrderSummary:
    subtotal: Decimal
    shipping: Decimal
    tax: Decimal
    total: Decimal
    discount: Decimal = Decimal("0.00")


def _shipping_for(subtotal: Decimal) -> Decimal:
    if subtotal == 0 or subtotal >= config.FREE_SHIPPING_THRESHOLD:
        return Decimal("0.00")
    return config.SHIPPING_FEE


def calculate_total(cart: Cart) -> OrderSummary:
    """Work out what the customer pays for this cart."""
    subtotal = cart.subtotal
    shipping = _shipping_for(subtotal)
    tax = _money(subtotal * config.TAX_RATE)
    total = _money(subtotal + shipping + tax)
    return OrderSummary(subtotal=subtotal, shipping=shipping, tax=tax, total=total)


def checkout(cart: Cart, gateway: PaymentGateway, card_token: str) -> PaymentResult:
    if not cart.items:
        raise ValueError("Cart is empty")
    summary = calculate_total(cart)
    return gateway.charge(summary.total, card_token)
