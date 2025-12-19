# ✨ Django MailFlow
### Creative HTML Email Signup System

A beautifully crafted **Django-based email onboarding system** that sends **HTML welcome emails** using reusable templates and modern email delivery practices.

> Turn every signup into a great first impression 💌

---

## 🌈 Why Django MailFlow?

Most projects send boring text emails.  
**Django MailFlow** delivers **branded, HTML-based welcome emails** that feel professional, warm, and memorable.

---

## 🚀 Features

🎯 User Welcome form  
📨 HTML welcome email using Django templates  
🎨 Dynamic email content (username, year, branding)  
⚡ EmailMultiAlternatives support  
🔁 Redirect-based success handling  
🧼 Clean & minimal Django views  
📱 Email-client friendly design  

---

## 🛠️ Tech Stack

| Tool | Usage |
|----|-----|
| Django 6 | Backend framework |
| Python 3.12.3 | Core language |
| SMTP | Email delivery |
| HTML + CSS | Email template |


---

## 🧩 Core View Logic

```python
def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")

        context = {
            "site_name": "Raihan World",
            "user": {"first_name": first_name},
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

        return redirect('/?success=1')

    return render(request, "form.html")
```

🧪 Sample Success Message
```
🎉 Welcome email sent successfully!
```

📧 Email Template Variables

Your HTML email template supports dynamic Django variables:
```
Hello {{ user.first_name }},

Welcome to {{ site_name }} 🎉

© {{ current_year }}
```

⚙️ Email Configuration (SMTP)
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```


