from rest_framework import viewsets, mixins
from rest_framework.views import APIView

from blog.models import contentModel, rateModel
from blog.serializers import contentSerializer, rateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class contentViewSet( mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = contentModel.objects.all()
    serializer_class = contentSerializer
    permission_classes = (IsAuthenticated,)

class rateViewSet( mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = rateModel.objects.all()
    serializer_class = rateSerializer
    permission_classes = (IsAuthenticated,)




    
