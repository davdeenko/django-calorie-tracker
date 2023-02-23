from django.contrib.auth.models import User
from rest_framework import serializers
from food_consuming.models import Food, Consume


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['url', 'name', 'calories', 'carbs', 'proteins', 'fats']


class ConsumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consume
        fields = ['food_consumed', 'user']

