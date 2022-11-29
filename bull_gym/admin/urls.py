from django.urls import path
from admin import views

urlpatterns = [
    path("see-users/",views.UsersViews.as_view())
]
