
import uuid
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from .logger import get_logger

log = get_logger("product")


@dataclass
class Product:
    sku: str
    name: str 
    price: Decimal



def search_products(products, keyword):
        """Search for products by keyword in name or description."""
        keyword_lower = keyword.lower()
        return [
            product for product in products
            if keyword_lower in product.name.lower()
        ]
