from django.db import models

# Create your models here.

daraja = (
    ('easy','Osson'),
    ('normal',"O'rtacha"),
    ('hard','Qiyin'),
)

publish = (
    ('see',"Ko'rsatish"),
    ('notsee',"Yashirish")
)

class Quiz(models.Model):
    turi = models.CharField(max_length=120,choices=daraja,verbose_name="Qiyinlik darajasi")
    quiz = models.TextField(verbose_name="Savolni kiriting ")
    answer = models.CharField(max_length=300,verbose_name="To'g'ri javob")

    option1 = models.CharField(max_length=300,verbose_name="Birinchi variant")
    option2 = models.CharField(max_length=300,verbose_name="Ikkinchi variant")
    option3 = models.CharField(max_length=300,verbose_name="Uchinchi variant")
    option4 = models.CharField(max_length=300,verbose_name="To'ritnchi variant")

    status = models.CharField(max_length=120,choices=publish,verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer


