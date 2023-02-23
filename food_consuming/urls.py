from django.urls import path
from food_consuming import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('delete/<int:id>/', views.DeleteView.as_view(), name="delete"),
]
