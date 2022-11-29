from django.urls import path
from api import views

urlpatterns = [
    path(
        "loging-user/",
        views.LoginViews.as_view(),
    ),
    path("create-user/", views.CreateUserViews.as_view()),
    path("see-bookings/",views.BookingsListViews.as_view()),
    path("add-bookings/sink/",views.BookingsPiletaViews.as_view()),
    path("add-bookings/gym/",views.BookingsPiletaViews.as_view()),
    path("add-bookings/paddle/",views.BookingsPiletaViews.as_view()),
    path("add-bookings/futbol/",views.BookingsPiletaViews.as_view()),
    path("total-pay/",views.BookingsTotalPayViews.as_view())
]