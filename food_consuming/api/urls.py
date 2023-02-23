from django.urls import include, path
from rest_framework import routers
from food_consuming.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'consumes', views.ConsumeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]