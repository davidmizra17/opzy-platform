from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from . import services


class VisitorSessionAuthentication(BaseAuthentication):
    """Autentica al visitante con el token de sesión: `Authorization: Visitor <token>`."""

    keyword = "Visitor"

    def authenticate(self, request):
        header = request.headers.get("Authorization", "")
        if not header.startswith(f"{self.keyword} "):
            return None
        session = services.resolve_session(header.removeprefix(f"{self.keyword} ").strip())
        if session is None:
            raise AuthenticationFailed("Sesión inválida o vencida.")
        request.visitor_session = session
        return (None, session)
