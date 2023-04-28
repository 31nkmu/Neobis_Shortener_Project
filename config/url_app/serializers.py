import random
import string
from rest_framework import serializers

from url_app.models import Url


class UrlSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=True)

    class Meta:
        model = Url
        fields = '__all__'

    @staticmethod
    def validate_url(url):
        if Url.objects.filter(url=url).exists():
            raise serializers.ValidationError('Такая ссылка уже существует')
        return url

    def create(self, validated_data):
        while True:
            short_url = ''.join(
                random.choices(string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters, k=6))
            if not Url.objects.filter(short_url=short_url).exists():
                break
        validated_data.update({'short_url': short_url})
        url_obj = Url.objects.create(**validated_data)
        return url_obj


class GetFullLinkSerializer(serializers.Serializer):
    short_url = serializers.CharField(max_length=6, required=True, min_length=6)



