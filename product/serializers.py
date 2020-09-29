from rest_framework import serializers
from .models import UserProfile, Doctor


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','firebase_uid','user_name','birthday','gender','insurance_image','insurance_symbol','insurance_number','insurer_number',)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id','full_name','hospital_name','introduction_text','profile_image',)
