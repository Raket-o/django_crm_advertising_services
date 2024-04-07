from django.contrib.auth.views import LoginView
from django.urls import path

from .views import LogoutView

app_name = "authorization"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name='authorization/login.html',
            redirect_authenticated_user=True,
        ),
        name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
