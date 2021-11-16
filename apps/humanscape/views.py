from datetime import datetime, timedelta

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from apps.humanscape.models import ClinicalInfo
from apps.humanscape.serializers import ClinicalInfoSerialzers


class ClinicalInfoViewset(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerialzers
    permission_classes = [AllowAny]

    def filter_queryset(self, queryset):
        if self.action == "list":
            keyword = self.request.query_params.get("project_name")
            if keyword:
                queryset = self.get_queryset().filter(project_name__icontains=keyword)
        return super().filter_queryset(queryset)


class RecentlyUpdateListView(ListModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerialzers
    permission_classes = [AllowAny]

    def filter_queryset(self, queryset):
        if self.action == "list":
            time = datetime.now() - timedelta(weeks=1)
            queryset = queryset.filter(updated_at__gte=time)
            queryset = queryset.order_by("updated_at")
        return super().filter_queryset(queryset)
