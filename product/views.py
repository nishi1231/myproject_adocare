from rest_framework import generics
from .models import UserProfile, Doctor, Reservation, ReservationOtherChoice, DoctorReservationReception
from .serializers import UserProfileSerializer, DoctorSerializer, ReservationSerializer, ReservationOtherChoiceSerializer, DoctorReservationReceptionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pandas.io.json import json_normalize
from datetime import datetime, date, time, timedelta

import pandas as pd
import numpy as np
import pytz



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
    start_day_value = DoctorReservationReception.objects.values('start_day')
    end_day_value = DoctorReservationReception.objects.values('end_day')
    frequency_value = DoctorReservationReception.objects.values('frequency')


    frequency_value_list = list(frequency_value)

    frequency1 = [{'frequency':1}]
    frequency2 = [{'frequency':2}]
    frequency3 = [{'frequency':3}]

    if frequency_value_list == frequency1:
        reservation_frequency = 'B'
        print('営業日')

    elif frequency_value_list == frequency2:  
        reservation_frequency = 'W'
        print('隔週')
        # 開始日から計算いる。

    elif frequency_value_list == frequency3:  
        reservation_frequency = 'MS'
        print('毎月')
        # 開始日から計算いる

    else:  
        print('該当なし')
        reservation_frequency = 'D'
    
    

    start_day_value_diclist = list(start_day_value)
    end_day_value_diclist = list(end_day_value)

    start_day_value_listconvert = [d.get('start_day') for d in start_day_value_diclist]
    end_day_value_listconvert = [d.get('end_day') for d in end_day_value_diclist]

    for start_days in start_day_value_listconvert :
        print(start_days)

    for end_days in end_day_value_listconvert :
        print(end_days)


    td = date.today()
    two_weeks = td + timedelta(days=14)


    if end_days < two_weeks:
        end_pd = end_days

    elif end_days > two_weeks:
        end_pd = two_weeks
        print('終わり日はまだ先')
    
    else:  
        print('該当なし')


    reservation_datelist = pd.Series(pd.date_range(start=start_days, end=end_pd, freq=reservation_frequency).normalize(),
          name='Date')
    print(reservation_datelist)
    print(reservation_datelist.dt.dayofweek)

    # JSON変換してcontextにわたす必要あるかも。

    reservation_dates = reservation_datelist.to_dict()
    print(reservation_dates)

    def get_serializer_context(self, reservation_dates):
        context = super().get_serializer_context()
        context['reservation_dates'] = reservation_dates
        return context


    


    




