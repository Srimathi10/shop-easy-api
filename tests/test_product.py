
from decimal import Decimal
from src.product import Product, search_products

products = [
    Product("SKU-100", "Coffee beans", 12.50),
    Product("SKU-200", "French press", 29.00),
    Product("SKU-300", "Espresso machine", 199.00),
    Product("SKU-400", "Tea kettle", 45.00),
]

def test_exact_search():
    results = search_products(products, "Coffee beans")
    assert len(results) == 1


def test_partial_search():
    results = search_products(products, "machine")
    assert len(results) == 1


def test_case_insensitive_search():
    results = search_products(products, "PRESS")
    assert len(results) == 2


def test_no_results():
    results = search_products(products, "xyz")
    assert results == []