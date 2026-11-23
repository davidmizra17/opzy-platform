class PageError(Exception):
    """Error de dominio de páginas."""


class InvalidPatch(PageError):
    """Las operaciones no se pueden aplicar al documento."""


class InvalidDocument(PageError):
    """El documento resultante no cumple el esquema."""

    def __init__(self, errors: list[str]):
        super().__init__("; ".join(errors))
        self.errors = errors


class UnsupportedClaims(PageError):
    """El texto afirma datos que el cliente no dio."""

    def __init__(self, claims: list[str]):
        super().__init__(", ".join(claims))
        self.claims = claims
