from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
daraja = (
    ('osson','Ossonroq'),
    ("o'rtacha","O'rtacha"),
    ('qiyin','Qiyin')
)

class Riddle(models.Model):
    riddle = models.TextField(verbose_name="Topishmoq qanday")
    holati = models.CharField(max_length=50,choices=daraja)
    javobi = models.CharField(max_length=80)
    vaqti = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.javobi

