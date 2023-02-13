from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsReedPermisions
from .models import Riddle
from .serializer import SerRidle
# Create your views here.

class ListAPI(ListAPIView):
    # permission_classes = (IsReedPermisions,)
    queryset = Riddle.objects.all()
    serializer_class = SerRidle


class CreateListAPI(ListCreateAPIView):
    permission_classes = (IsReedPermisions,)
    queryset = Riddle.objects.all()
    serializer_class = SerRidle


class DetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReedPermisions,IsAuthenticated,)
    queryset = Riddle.objects.all()
    serializer_class = SerRidle
    
