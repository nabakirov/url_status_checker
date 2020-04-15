from rest_framework import serializers as s
from . import models


class UrlSerializer(s.ModelSerializer):
    class Meta:
        model = models.Url
        fields = ('id', 'url')
