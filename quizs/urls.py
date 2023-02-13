from django.urls import path
from .views import *

urlpatterns = [
    path('',QuizListAPI.as_view()),
    path('easy/',EasyListApi.as_view()),
    path('normal/',NormalListApi.as_view()),
    path('hard/',HardListApi.as_view()),
    
]