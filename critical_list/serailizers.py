from rest_framework import serializers

from critical_list.models import Part


class PartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Part
        fields='__all__'