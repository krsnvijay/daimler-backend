from rest_framework import serializers

from accounts.models import Subscription
from critical_list.models import Part
from sos.models import Comment


class PartSerializer(serializers.HyperlinkedModelSerializer):
    part_number = serializers.CharField(max_length=30, required=True)
    starred = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Part
        fields='__all__'

    def get_starred(self, obj):
        user = self.context['request'].user
        return user.starred_parts.filter(part_number=obj.part_number).exists()

    def get_comments(self, obj):
        return Comment.objects.filter(partid=obj.part_number, type=False).count()


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
