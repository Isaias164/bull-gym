from django.urls import path
from admin import views

urlpatterns = [
    path("see-users/",views.UsersViews.as_view()),
    path("see-bookings/",views.BookingsViews.as_view()),
    path("see-bookings-free/",views.BookingsFreeView.as_view()),
    path("see-bookings-user/",views.BookingsUsers().as_view()),
    path("see-futbol/",views.FutbolViews.as_view()),
    path("see-paddle/",views.PaddleViews.as_view()),
    path("see-sink/",views.SinksViews.as_view()),
    path("see-gym/",views.GymViews.as_view()),
]
