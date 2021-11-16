from django_filters import rest_framework as filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from apps.humanscape.filters import ClinialInfoRecentlyUpdateFilter
from apps.humanscape.models import ClinicalInfo
from apps.humanscape.serializers import (
    ClinicalInfoSerialzers,
    RecentlyUpdateListSerializer,
)


class ClinicalInfoViewset(RetrieveModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerialzers
    permission_classes = [AllowAny]
    lookup_field = "pk"
   
class RecentlyUpdateListView(ListModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = RecentlyUpdateListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ClinialInfoRecentlyUpdateFilter
