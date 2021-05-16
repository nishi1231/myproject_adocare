from rest_framework import generics
from .models import UserProfile, Doctor, Reservation, ReservationOtherChoice, DoctorReservationReception
from .serializers import UserProfileSerializer, DoctorSerializer, ReservationSerializer, ReservationOtherChoiceSerializer, DoctorReservationReceptionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# 日付取得のテストで記載
import pandas as pd
import numpy as np


class UserProfile(generics.ListCreateAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserProfile, self).dispatch(request, *args, **kwargs)

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class Reservation(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationOtherChoice(generics.ListCreateAPIView):
    queryset = ReservationOtherChoice.objects.all()
    serializer_class = ReservationOtherChoiceSerializer


class DoctorReservationReception(generics.ListCreateAPIView):
    queryset = DoctorReservationReception.objects.all()
    serializer_class = DoctorReservationReceptionSerializer
    frequency_value = DoctorReservationReception.objects.values('frequency')

    frequency_value_list = list(frequency_value)
    print(frequency_value_list)


    # todayをmodelの開始日で代入。
    # 14日先の日付けまで出す。隔週の場合、営業日などでperiodsを変換。
    # 時間も計算する　https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11185745136
    #　医師を選択するとリレーションされた予約日時がレスポンスを返すように。　https://selfnote.work/20200531/programming/django-rest-framework-basic7/
    

    frequency1 = [{'frequency':1}]
    frequency2 = [{'frequency':2}]
    frequency3 = [{'frequency':3}]

    if frequency_value_list == frequency1:
        reservation_frequency = 'B'
        print('営業日')

    elif frequency_value_list == frequency2:  
        reservation_frequency = 'W'
        print('隔週')

    elif frequency_value_list == frequency3:  
        reservation_frequency = 'MS'
        print('毎月')

    else:  
        print('該当なし')
        reservation_frequency = 'D'
    

    datelist = pd.Series(pd.date_range('today', periods=14, freq=reservation_frequency).normalize(),
          name='Date')
    print(datelist)
    print(datelist.dt.dayofweek)
