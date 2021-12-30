from rest_framework import serializers

class NewsSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=250, verbose_name='Наименование')
    content = serializers.CharField(max_length=250, verbose_name='Контент')
    created_at = serializers.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')