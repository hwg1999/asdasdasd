from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage
from meiduo_admin.serialziers.images import ImagesSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser


class ImagesView(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImagesSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]
