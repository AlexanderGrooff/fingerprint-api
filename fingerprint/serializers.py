from rest_framework import serializers


class FingerprintSerializer(serializers.Serializer):
    components = serializers.JSONField()
    hash = serializers.CharField(max_length=50)
    seen_counter = serializers.IntegerField()
