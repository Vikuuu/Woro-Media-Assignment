from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

def send_confirmation_email(email):
    user = User.objects.get(email=email)
    user_name = user.retrieve_username()
    company_name = "Woro Media"

    subject = f"Action Required: Verify Your Email for {company_name}"
    
    verify_url = reverse('verify-email', kwargs={'token': user.confirmation_token})

    message = f"""
    Dear {user.username},

    Thank you for registering with {company_name}! To complete the registration process and ensure the security of your account, we need to verify your email address.

    Please click on the following link to verify your account:
    
    {settings.BASE_URL}{verify_url}

    If you did not initiate this registration, please disregard this email.

    Thank you for choosing {company_name}. We look forward to serving you!

    Best regards,
    {company_name}
    """

    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [user.email])
    
    