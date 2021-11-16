from rest_framework import serializers

from .model import ClinicalInfo

class ClinicalInfoSerialzers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalInfo
        fields = '__all__'