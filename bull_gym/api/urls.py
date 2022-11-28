from django.urls import path
from .views import LoginViews, CreateUserViews,BookingsListViews,BookingsPiletaViews

urlpatterns = [
    path(
        "loging-user/",
        LoginViews.as_view(),
    ),
    path("create-user/", CreateUserViews.as_view()),
    path("see-bookings/",BookingsListViews.as_view()),
    path("add-bookings/pileta/",BookingsPiletaViews.as_view())
]


# urlpatterns = [
#     path("create/user/", create_user, name="create-user"),
#     path("loging/user/", validate_user, name="loging-user"),
#     path("user/delete/", login, name="delete-user"),
#     path("user/data/", login, name="get-data"),
#     path("update/email/", update_email, name="update-email"),
#     path("update/password/", update_password, name="update-password"),
#     path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
# ]
