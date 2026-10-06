"""Outgoing email.

In development and tests nothing is really sent: messages are kept in
``EmailService.outbox`` so they can be inspected.
"""
from dataclasses import dataclass
from typing import List

from . import config
from .logger import get_logger

log = get_logger("email")


@dataclass
class Email:
    to: str
    subject: str
    body: str
    sender: str = config.SUPPORT_EMAIL


class EmailService:
    def __init__(self) -> None:
        self.outbox: List[Email] = []

    def send(self, to: str, subject: str, body: str) -> Email:
        message = Email(to=to, subject=subject, body=body)
        self.outbox.append(message)
        log.info("Email queued: %r", subject)
        return message
