"""Puerto del proveedor de pagos. La implementación concreta se elige en settings."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class CheckoutSession:
    provider_reference: str
    url: str


class PaymentProvider(Protocol):
    def create_checkout(
        self, *, amount_cents: int, currency: str, description: str, idempotency_key: str
    ) -> CheckoutSession: ...

    def verify_webhook(self, *, payload: bytes, signature: str) -> dict: ...
