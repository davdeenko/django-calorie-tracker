from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from food_consuming.api.serializers import UserSerializer, FoodSerializer, ConsumeSerializer
from food_consuming.models import Food, Consume


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [permissions.IsAuthenticated]
