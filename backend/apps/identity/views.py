from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services
from .serializers import StartSessionIn, StartSessionOut


class StartSessionView(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(request=StartSessionIn, responses=StartSessionOut)
    def post(self, request):
        data = StartSessionIn(data=request.data)
        data.is_valid(raise_exception=True)
        session = services.start_session(
            visitor_id=data.validated_data.get("visitor_id"),
            utm=data.validated_data["utm"],
            user_agent=request.headers.get("User-Agent", ""),
        )
        return Response(
            StartSessionOut(
                {"visitor_id": session.visitor_id, "session_id": session.id, "token": session.token}
            ).data,
            status=201,
        )
