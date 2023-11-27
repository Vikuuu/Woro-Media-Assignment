from django.urls import path
from .views import RegistrationView, LoginView, VerifyEmailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path("api/register/", cache_page(10)(RegistrationView.as_view())),
    path("api/login/", cache_page(10)(LoginView.as_view()), name="token_obtain_pair"),
    path(
        "api/login/refresh/",
        cache_page(10)(TokenRefreshView.as_view()),
        name="token_refresh",
    ),
    path(
        "verify-email/<str:token>/",
        cache_page(10)(VerifyEmailView.as_view()),
        name="verify-email",
    ),
]
