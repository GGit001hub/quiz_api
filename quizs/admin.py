from django.contrib import admin
from .models import Quiz
# Register your models here.

@admin.register(Quiz)
class QuizRegister(admin.ModelAdmin):
    list_display = ['turi','answer','status','created_at']
    list_filter = ['turi','status','created_at']
    search_fields = ['answer',]
