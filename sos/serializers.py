from rest_framework import serializers

from sos.models import Sos, Comment


class SoSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sos
        fields='__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
