from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.identity.authentication import VisitorSessionAuthentication

from . import services


class EventIn(serializers.Serializer):
    event_id = serializers.UUIDField()
    name = serializers.CharField(max_length=64)
    occurred_at = serializers.DateTimeField()
    source = serializers.ChoiceField(choices=["landing", "widget"])
    path = serializers.CharField(max_length=500, required=False, allow_blank=True)
    props = serializers.DictField(required=False, default=dict)


class EventBatchIn(serializers.Serializer):
    events = EventIn(many=True, max_length=100)


class EventIngestView(APIView):
    authentication_classes = [VisitorSessionAuthentication]
    permission_classes = []

    @extend_schema(request=EventBatchIn, responses={202: None})
    def post(self, request):
        data = EventBatchIn(data=request.data)
        data.is_valid(raise_exception=True)
        session = request.visitor_session
        rejected = []
        for item in data.validated_data["events"]:
            try:
                services.record(
                    item["name"],
                    event_id=item["event_id"],
                    occurred_at=item["occurred_at"],
                    source=item["source"],
                    visitor_id=session.visitor_id,
                    session_id=session.id,
                    path=item.get("path", ""),
                    props=item["props"],
                )
            except services.UnknownEvent:
                rejected.append(str(item["event_id"]))
        return Response({"rejected": rejected}, status=202)
