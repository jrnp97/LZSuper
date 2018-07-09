from django.contrib.auth.models import User
from rest_framework import serializers

from robots.models import RSeoStatus


class RSeoStatusSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='robots:rseostatus-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = RSeoStatus
        fields = (
            'id',
            'url',
            'owner',
            'keyword',
            'domain',
            'google',
            'yahoo',
            'bing',
            'duckduck',
            'destination'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='robots:user-detail')
    rseostatus = serializers.HyperlinkedRelatedField(many=True, view_name='robots:rseostatus-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'username',
            'get_full_name',
            'rseostatus'
        )

