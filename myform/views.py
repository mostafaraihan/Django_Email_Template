from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import now

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")

        context = {
            "site_name": "Raihan World",
            "user": {
                "first_name": first_name
            },
            "current_year": now().year,
        }

        html_content = render_to_string("massage.html", context)

        email_message = EmailMultiAlternatives(
            subject="Welcome to Raihan World!",
            body="Welcome to Raihan World!",
            from_email="Raihan World <noreply@raihanworld.com>",
            to=[email],
        )

        email_message.attach_alternative(html_content, "text/html")
        email_message.send()

        return render(request, "form.html", {
            "message": "Welcome email sent successfully!"
        })

    return render(request, "form.html")
