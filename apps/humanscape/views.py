<<<<<<< HEAD
from app.humanscape.models import ClinicalInfo
from app.humanscape.serializers import ClinicalInfoSerialzers
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class ClinicalInfoViewset(RetrieveModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerialzers
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object(kwargs["pk"])
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
=======
from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from apps.humanscape.filters import ClinialInfoRecentlyUpdateFilter
from apps.humanscape.models import ClinicalInfo
from apps.humanscape.serializers import RecentlyUpdateListSerializer


class RecentlyUpdateListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = RecentlyUpdateListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ClinialInfoRecentlyUpdateFilter
>>>>>>> 59fbf06 (FEAT: Add Recently Update List API)
