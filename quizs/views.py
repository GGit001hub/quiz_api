from django.shortcuts import render
from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer
from .pemisions import *
# Create your views here.

class QuizListAPI(generics.ListAPIView):
    queryset = Quiz.objects.filter(status="see")
    serializer_class = QuizSerializer

class EasyListApi(generics.ListAPIView):
    queryset = Quiz.objects.filter(turi='easy')
    serializer_class = QuizSerializer

class NormalListApi(generics.ListAPIView):
    queryset = Quiz.objects.filter(turi='normal')
    serializer_class = QuizSerializer


class HardListApi(generics.ListAPIView):
    queryset = Quiz.objects.filter(turi='hard')
    serializer_class = QuizSerializer

