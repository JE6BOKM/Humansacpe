from rest_framework.viewsets    import GenericViewSet
from rest_framework.mixins      import RetrieveModelMixin
from rest_framework.response    import Response
from rest_framework.permissions import AllowAny

from .models      import ClinicalInfo
from .serializers import ClinicalInfoSerialzers

class ClinicalInfoViewset(RetrieveModelMixin, GenericViewSet):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerialzers
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object(kwargs['pk'])
        serializer = self.get_serializer(instance)

        return Response(serializer.data)