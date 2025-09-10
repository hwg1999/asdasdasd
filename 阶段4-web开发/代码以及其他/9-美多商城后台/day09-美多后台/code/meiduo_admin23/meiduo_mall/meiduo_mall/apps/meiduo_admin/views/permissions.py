from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serialziers.permissions import PerssionsSerialzier
from meiduo_admin.utils import PageNum


class PermissionsView(ModelViewSet):
    serializer_class = PerssionsSerialzier
    queryset = Permission.objects.all()
    pagination_class = PageNum
    permission_classes = [IsAdminUser]
