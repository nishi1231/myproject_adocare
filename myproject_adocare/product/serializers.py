from rest_framework import serializers
from .models import UserProfile, Doctor, Reservation, ReservationOtherChoice, DoctorReservationReception



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','user_name','user_name','birthday','gender','insurance_image','insurance_symbol','insurance_number','insurer_number',)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id','full_name','hospital_name','introduction_text','profile_image',)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('user','doctor','temperature','cough','period','datetime',)


class ReservationOtherChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationOtherChoice
        fields = ('reservation','headache','runnynose','jointpain','dizzy','palpitations','stomachache','nausea',)


class DoctorReservationReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorReservationReception
        fields = ('doctor','day_of_the_week','frequency','start_day','end_day','start_time','end_time','active',)
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['reservation_dates']= self.context[reservation_dates]
        return ret


