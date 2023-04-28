from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from url_app.models import Url
from url_app.serializers import UrlSerializer, GetFullLinkSerializer


class UrlViewSet(CreateModelMixin,
                 DestroyModelMixin,
                 ListModelMixin,
                 GenericViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class GetFullLinkAPIView(APIView):
    def post(self, request):
        serializer = GetFullLinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url = request.data['short_url']
        url = Url.objects.filter(short_url=short_url)
        if url.exists():
            return Response({'full_url': url[0].url}, status=status.HTTP_200_OK)
        return Response({'msg': 'нет такой ссылки'}, status=status.HTTP_400_BAD_REQUEST)
