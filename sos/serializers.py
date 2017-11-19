from django.utils import timezone
from rest_framework import serializers

from sos.models import Sos, Comment


class SoSSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    posted_by = serializers.CharField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    date = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now)
    )
    subscribed = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    class Meta:
        model = Sos
        fields = '__all__'

    def get_subscribed(self, obj):
        user = self.context['request'].user
        return obj.users.filter(id=user.id).exists()

    def get_comments_count(self, obj):
        return Comment.objects.filter(sosid=obj.id).count()
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
