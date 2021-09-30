from django.contrib import admin

from .models import UserProfile
from .models import Doctor
from .models import Reservation
from .models import ReservationOtherChoice
from .models import DoctorReservationReception

admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(Reservation)
admin.site.register(ReservationOtherChoice)
admin.site.register(DoctorReservationReception)
