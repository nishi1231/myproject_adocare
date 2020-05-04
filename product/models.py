from django.db import models

from django.conf import settings
from django.utils import timezone

class Doctor(models.Model):
    full_name = models.CharField(max_length=30,verbose_name='氏名')
    hospital_name = models.CharField(max_length=30,verbose_name='病院名')
    introduction_text = models.TextField(max_length=1000,verbose_name='紹介文')
    profile_image = models.ImageField(upload_to='documents/', default='defo',verbose_name='画像')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.full_name
