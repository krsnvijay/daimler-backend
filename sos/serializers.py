from django.utils import timezone
from rest_framework import serializers

from sos.models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    posted_by = serializers.CharField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    date = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now)
    )


    class Meta:
        model = Comment
        fields = '__all__'


class PartNotificationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    posted_by = serializers.CharField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    date = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now)
    )

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'userid': {'required': True}, 'partid': {'required': True}}
