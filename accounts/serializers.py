from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# first we define the serializers
from accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class LogEntrySerializer(serializers.HyperlinkedModelSerializer):
    content_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='model'
    )

    class Meta:
        model = LogEntry
        fields = '__all__'
