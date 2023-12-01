from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from user_app.views import HomeView, SignUpView, CodeVerificationView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "login/",
        LoginView.as_view(template_name="login.html", redirect_authenticated_user=True),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("verify/", CodeVerificationView.as_view(), name="verify"),
    path("", HomeView.as_view(), name="home"),
]
