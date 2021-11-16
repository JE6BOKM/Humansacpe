<<<<<<< HEAD
from app.humanscape.model import ClinicalInfo
from rest_framework import serializers


class ClinicalInfoSerialzers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalInfo
        fields = "__all__"
=======
from rest_framework import serializers

from apps.humanscape.models import ClinicalInfo


class RecentlyUpdateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalInfo
        fields = "__all__"
<<<<<<< HEAD
>>>>>>> 59fbf06 (FEAT: Add Recently Update List API)
=======
>>>>>>> 4d1f3a0 (STYLE: Edit Conventions)
