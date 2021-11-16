from app.humanscape.model import ClinicalInfo
from rest_framework import serializers


class ClinicalInfoSerialzers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalInfo
        fields = "__all__"
