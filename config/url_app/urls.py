from django.urls import path
from rest_framework.routers import DefaultRouter

from url_app import views

router = DefaultRouter()
router.register('', views.UrlViewSet)


urlpatterns = [
    path('full/', views.GetFullLinkAPIView.as_view()),
]

urlpatterns += router.urls
