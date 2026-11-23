from rest_framework import serializers


class StartSessionIn(serializers.Serializer):
    visitor_id = serializers.UUIDField(required=False, allow_null=True)
    utm = serializers.DictField(child=serializers.CharField(), required=False, default=dict)


class StartSessionOut(serializers.Serializer):
    visitor_id = serializers.UUIDField()
    session_id = serializers.UUIDField()
    token = serializers.CharField()
