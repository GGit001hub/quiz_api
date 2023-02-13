from rest_framework import serializers
from .models import Riddle


class SerRidle(serializers.ModelSerializer):
    class Meta:
        model = Riddle
        fields = ['id','riddle','holati','javobi','author']




