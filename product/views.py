from rest_framework import generics
from .models import UserProfile, Doctor, Reservation, ReservationOtherChoice
from .serializers import UserProfileSerializer, DoctorSerializer, ReservationSerializer, ReservationOtherChoiceSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserProfile(generics.CreateAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserProfile, self).dispatch(request, *args, **kwargs)

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class Reservation(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationOtherChoice(generics.CreateAPIView):
    queryset = ReservationOtherChoice.objects.all()
    serializer_class = ReservationOtherChoiceSerializer


    