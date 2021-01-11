from rest_framework import serializers
from .models import GoodsModel


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsModel
        fields = '__all__'
