from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from jsonfield import JSONField
from django.conf import settings
from django.utils import timezone


GENDER_CHOICES = [
    ('1', '男性'),
    ('2', '女性'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) 
    user_name = models.CharField(blank=True,null=True,max_length=30,verbose_name='氏名', default='')
    birthday = models.DateField(blank=True,null=True)
    gender = models.CharField(blank=True,null=True,verbose_name='性別', default='', max_length=1, choices=GENDER_CHOICES)
    insurance_image = models.ImageField(blank=True,null=True,upload_to='documents/', default='defo',verbose_name='保険証画像')
    insurance_symbol = models.IntegerField(blank=True,null=True,verbose_name='保険証記号',default=0, validators=[MinValueValidator(1), MaxValueValidator(100000000)])
    insurance_number = models.IntegerField(blank=True,null=True,verbose_name='保険証番号',default=0, validators=[MinValueValidator(1), MaxValueValidator(100000000)])
    insurer_number = models.IntegerField(blank=True,null=True,verbose_name='保険者番号',default=0, validators=[MinValueValidator(1), MaxValueValidator(100000000)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Doctor(models.Model):
    full_name = models.CharField(max_length=30,verbose_name='氏名')
    hospital_name = models.CharField(max_length=30,verbose_name='病院名')
    introduction_text = models.TextField(max_length=1000,verbose_name='紹介文')
    profile_image = models.ImageField(upload_to='documents/', default='defo',verbose_name='画像')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ManyToManyField(Doctor)
    temperature = models.FloatField(validators=[MinValueValidator(35.0), MaxValueValidator(42.0)])
    cough = models.BooleanField(default=True)
    period = models.IntegerField(blank=True,null=True,verbose_name='日数', validators=[MinValueValidator(1), MaxValueValidator(365)])
    datetime = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReservationOtherChoice(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    headache = models.BooleanField(default=True)
    runnynose = models.BooleanField(default=True)
    jointpain = models.BooleanField(default=True)
    dizzy = models.BooleanField(default=True)
    palpitations = models.BooleanField(default=True)
    stomachache = models.BooleanField(default=True)
    nausea = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class DoctorReservationReception(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_the_week = models.JSONField(blank=True, null=True)
    # 0:月,1:火,2:水,3:木,4:金,5:土,6:日
    frequency = models.JSONField(blank=True, null=True)
    # 0:営業日のみ毎日,1:1週間ごと,2:毎月
    start_day = models.DateField(blank=True,null=True,verbose_name='受付開始日')
    end_day = models.DateField(blank=True,null=True,verbose_name='受付終了日')
    start_time = models.TimeField(blank=True,null=True,verbose_name='受付開始時間')
    end_time = models.TimeField(blank=True,null=True,verbose_name='受付終了時間')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __str__(self):
     #  return self.full_name
