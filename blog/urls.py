from django.urls import path
from rest_framework import routers
from blog import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'content', views.contentViewSet)
router.register(r'rate', views.rateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

