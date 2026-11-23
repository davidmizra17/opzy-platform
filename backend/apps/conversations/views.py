from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.exceptions import NotFound, Throttled
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.identity.authentication import VisitorSessionAuthentication

from . import services
from .models import Conversation


class StartConversationIn(serializers.Serializer):
    language = serializers.ChoiceField(choices=["es", "en"], default="es")


class MessageIn(serializers.Serializer):
    text = serializers.CharField(max_length=4000)


class StartConversationView(APIView):
    authentication_classes = [VisitorSessionAuthentication]
    permission_classes = []

    @extend_schema(request=StartConversationIn, responses={201: None})
    def post(self, request):
        data = StartConversationIn(data=request.data)
        data.is_valid(raise_exception=True)
        try:
            conversation = services.start_conversation(
                visitor_id=request.visitor_session.visitor_id,
                language=data.validated_data["language"],
            )
        except services.LimitReached as exc:
            raise Throttled(detail=str(exc)) from exc
        return Response({"conversation_id": conversation.id}, status=201)


class MessageView(APIView):
    authentication_classes = [VisitorSessionAuthentication]
    permission_classes = []

    @extend_schema(request=MessageIn, responses={202: None})
    def post(self, request, conversation_id):
        conversation = Conversation.objects.filter(
            id=conversation_id, visitor_id=request.visitor_session.visitor_id
        ).first()
        if conversation is None:
            raise NotFound()
        data = MessageIn(data=request.data)
        data.is_valid(raise_exception=True)
        message = services.add_client_message(conversation, data.validated_data["text"])
        # TODO(fase-1): encolar el turno del agente (apps.triage) y transmitirlo por SSE.
        return Response({"message_id": message.id}, status=202)
