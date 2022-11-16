from rest_framework import serializers
from blog.models import contentModel, rateModel
import logging
import datetime
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

# class CategorySerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = CategoryModel
#         fields="__all__"

class contentSerializer(serializers.ModelSerializer):
    myRate = serializers.SerializerMethodField()

    def get_myRate(self, keyword):
        try:
            user =  self.context['request'].user
            try:
                return rateModel.objects.get(user = user,content=keyword).rate
            except ObjectDoesNotExist: 
                return "Please register your rate"
        except:
            return None

    class Meta:
        model = contentModel
        fields = ('id','title', 'description', 'numberOfRates', 'averageRate','myRate')
        read_only_fields = ['averageRate','numberOfRates','myRate']

class rateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user =  self.context['request'].user


        rate, created = rateModel.objects.update_or_create(
            user=user,
            defaults={**validated_data})
        if created:
            logger.info(
                f"rate created. id: {rate.id}" + str(datetime.datetime.now()),
                )
        else:
            logger.info(
                f"rate updated. id: {rate.id}" + str(datetime.datetime.now()),
                )
        return rate

    class Meta:
        model = rateModel
        fields = ('id', 'content', 'rate')
