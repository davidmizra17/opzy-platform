from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.identity.authentication import VisitorSessionAuthentication
from apps.pages.infrastructure.models import Page
from apps.pages.infrastructure.repository import page_use_cases


class PageOut(serializers.Serializer):
    page_id = serializers.UUIDField()
    version = serializers.IntegerField()
    document = serializers.JSONField()


class RevertIn(serializers.Serializer):
    to_version = serializers.IntegerField(min_value=1)
    base_version = serializers.IntegerField(min_value=1)


def _own_page(request, page_id) -> Page:
    page = Page.objects.filter(id=page_id, visitor_id=request.visitor_session.visitor_id).first()
    if page is None:
        raise NotFound()
    return page


def _out(snapshot) -> dict:
    return PageOut(
        {"page_id": snapshot.page_id, "version": snapshot.version, "document": snapshot.document}
    ).data


class PageView(APIView):
    authentication_classes = [VisitorSessionAuthentication]
    permission_classes = []

    @extend_schema(responses=PageOut)
    def get(self, request, page_id):
        _own_page(request, page_id)
        return Response(_out(page_use_cases().repo.get(page_id)))


class RevertPageView(APIView):
    authentication_classes = [VisitorSessionAuthentication]
    permission_classes = []

    @extend_schema(request=RevertIn, responses=PageOut)
    def post(self, request, page_id):
        _own_page(request, page_id)
        data = RevertIn(data=request.data)
        data.is_valid(raise_exception=True)
        snapshot = page_use_cases().revert_page(page_id, **data.validated_data)
        return Response(_out(snapshot))
