from rest_framework import serializers
from goods.models import SKUImage


class ImagesSerializer(serializers.ModelSerializer):
    """
        图片序列化器
    """
    sku_id = serializers.IntegerField()
    class Meta:
        model = SKUImage
        fields = "__all__"
