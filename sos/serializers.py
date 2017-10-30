from rest_framework import serializers
from sos.models import Sos
class SoSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sos
        fields='__all__'