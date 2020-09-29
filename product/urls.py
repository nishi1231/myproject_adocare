from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
  path("userprofile",views.UserProfile.as_view(), name="product"),
  path("doctorlist",views.DoctorList.as_view(), name="product"),
]
