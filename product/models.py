from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone


GENDER_CHOICES = [
    ('1', '男性'),
    ('2', '女性'),
]


class UserProfile(models.Model):
    firebase_uid = models.IntegerField(verbose_name='firebase_uid', validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    user_name = models.CharField(blank=True,null=True,max_length=30,verbose_name='氏名')
    birthday = models.DateField(blank=True,null=True)
    gender = models.CharField(blank=True,null=True,verbose_name='性別', max_length=1, choices=GENDER_CHOICES)
    insurance_image = models.ImageField(blank=True,null=True,upload_to='documents/', default='defo',verbose_name='保険証画像')
    insurance_symbol = models.IntegerField(blank=True,null=True,verbose_name='保険証記号', validators=[MinValueValidator(1), MaxValueValidator(100000000)])
    insurance_number = models.IntegerField(blank=True,null=True,verbose_name='保険証番号', validators=[MinValueValidator(1), MaxValueValidator(100000000)])
    insurer_number = models.IntegerField(blank=True,null=True,verbose_name='保険者番号', validators=[MinValueValidator(1), MaxValueValidator(100000000)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
