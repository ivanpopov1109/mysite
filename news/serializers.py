from rest_framework import serializers

class NewsSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField(max_length=250)
    created_at = serializers.DateTimeField()