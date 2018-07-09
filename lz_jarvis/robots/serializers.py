from rest_framework import serializers

from robots.models import RSeoStatus


class RSeoStatusSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='robots:rseostatus-detail')

    class Meta:
        model = RSeoStatus
        fields = (
            'id',
            'url',
            'keyword',
            'domain',
            'google',
            'yahoo',
            'bing',
            'duckduck',
            'destination'
        )
