from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import Certificate
from django.http import Http404


def index(request):
    return render(request, 'portfolio/index.html')


def about(request):
    certificates = Certificate.objects.all()
    context = {
        "title": "About Me",
        "subtitle": "Django app with editing, version control & permissions",
        "certificates": certificates,
    }
    return render(request, "portfolio/about.html", context)


# Example hardcoded projects (you can later make a Project model in models.py)
PROJECTS = {
    "file-management-system": {
        "title": "File Management System",
        "subtitle": "Django app with editing, version control & permissions",
        "description": "This project is a full file management platform built with Django...",
        "stack": ["Django", "PostgreSQL", "JavaScript"],
        "link": "https://github.com/yourusername/file-management-system",
        "image": None,  # replace with ImageField later
    },
    "medical-ai-assistant": {
        "title": "Medical AI Assistant",
        "subtitle": "AI-assisted image analysis with Django REST API",
        "description": "This app uses AI to scan medical images...",
        "stack": ["Django", "REST API", "AI/ML"],
        "link": "https://github.com/yourusername/medical-ai-assistant",
        "image": None,
    },
}


def projects(request):
    return render(request, "portfolio/projects.html", {"projects": PROJECTS})


def project_detail(request, slug):
    project = PROJECTS.get(slug)
    if not project:
        raise Http404("Project not found")
    return render(request, "portfolio/project_detail.html", {"project": project})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Send email
            send_mail(
                subject=f"Portfolio Contact from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email="rostomsiervo14@gmail.com",  # use your own domain email
                recipient_list=["rostomsierv14@gmail.com"]
            )


            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {"form": form})
