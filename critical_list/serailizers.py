from rest_framework import serializers

from critical_list.models import Part


class PartSerializer(serializers.HyperlinkedModelSerializer):
    part_number = serializers.CharField(max_length=30, required=True)
    starred = serializers.SerializerMethodField()
    class Meta:
        model = Part
        fields='__all__'

    def get_starred(self, obj):
        user = self.context['request'].user
        return user.starred_parts.filter(part_number=obj.part_number).exists()
