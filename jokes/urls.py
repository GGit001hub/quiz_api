from django.urls import path
from .views import ListAPI,DetailAPI,CreateListAPI
urlpatterns = [
    path('<int:pk>/',DetailAPI.as_view()),
    path('create/',CreateListAPI.as_view()),
    path('',ListAPI.as_view()),
]

