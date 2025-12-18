from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import now

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")

        # Email context
        context = {
            "site_name": "MyApp",
            "user": {"first_name": first_name},
            "login_url": "https://myapp.com/login/",
            "current_year": now().year,
            "company_address": "123 Main Street, City, Country",
        }

        # Render welcome email template
        html_content = render_to_string("emails/welcome_email.html", context)

        # Send email
        email_message = EmailMultiAlternatives(
            subject="Welcome to MyApp!",
            body="Welcome to MyApp!",
            from_email="MyApp <noreply@myapp.com>",
            to=[email],
        )
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()

        return render(request, "signup.html", {
            "message": "Welcome email sent successfully!"
        })

    return render(request, "signup.html")
