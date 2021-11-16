from django_filters import rest_framework as filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.humanscape.filters import ClinialInfoRecentlyUpdateFilter
from apps.humanscape.models import ClinicalInfo
from apps.humanscape.serializers import (
    ClinicalInfoSerialzers,
    RecentlyUpdateListSerializer,
)


class ClinicalInfoViewset(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerialzers
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(kwargs["pk"])
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def filter_queryset(self, queryset):
        if self.action == "list":
            keyword = self.request.query_params.get("trail_name")
            if keyword:
                queryset = self.get_queryset().filter(project_name__icontains=keyword)
        return super().filter_queryset(queryset)


class RecentlyUpdateListView(ListModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = RecentlyUpdateListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ClinialInfoRecentlyUpdateFilter
