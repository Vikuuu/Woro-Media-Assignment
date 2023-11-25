from django.urls import path
from .views import (
    RegistrationView, 
    LoginView, 
    VerifyEmailView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("api/register/", RegistrationView.as_view()),
    path('api/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
]