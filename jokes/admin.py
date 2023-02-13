from django.contrib import admin
from .models import Riddle
# Register your models here.

@admin.register(Riddle)
class RiddleAdmin(admin.ModelAdmin):
    list_display = ('javobi','id','holati','author','vaqti')
    list_filter = ('vaqti','holati')
