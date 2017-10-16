from rest_framework import serializers

from app.models import Part


class PartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Part
        fields='__all__'