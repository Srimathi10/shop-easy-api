"""Shared logging setup."""
import logging

_FORMAT = "%(asctime)s %(levelname)-7s [%(name)s] %(message)s"


def get_logger(name: str) -> logging.Logger:
    root = logging.getLogger("shopeasy")
    if not root.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(_FORMAT))
        root.addHandler(handler)
        root.setLevel(logging.INFO)
    return root.getChild(name)
