from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
  path("userprofile",views.UserProfile.as_view(), name="product"),
  path("doctorlist",views.DoctorList.as_view(), name="product"),
  path("reservation",views.Reservation.as_view(), name="product"),
  path("reservationotherchoice",views.ReservationOtherChoice.as_view(), name="product"),
]
