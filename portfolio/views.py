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
        "description": "Fully featured Django app with file editing, version control, and role-based permissions.",
        "stack": ["Django", "PostgreSQL", "JavaScript"],
        "link": "https://github.com/yourusername/file-management-system",
        "image": None,
    },
    "medical-ai-assistant": {
        "title": "Medical AI Assistant",
        "subtitle": "AI-assisted image analysis with Django REST API",
        "description": "AI-assisted image analysis platform with Django frontend and REST backend for healthcare support.",
        "stack": ["Django", "REST API", "AI"],
        "link": "https://github.com/yourusername/medical-ai-assistant",
        "image": None,
    },
    "dr-tom-ai": {
        "title": "Dr. Tom AI",
        "subtitle": "Gemini-powered medical assistant",
        "description": "A medical assistant powered by Gemini AI, providing real-time health insights and recommendations.",
        "stack": ["Gemini AI", "Python", "Django"],
        "link": "https://github.com/yourusername/dr-tom-ai",
        "image": None,
    },
    "smart-pos-system": {
        "title": "Smart POS System",
        "subtitle": "AI-powered Point of Sale system",
        "description": "Point of Sale system with AI-powered features for smarter sales, analytics, and inventory management.",
        "stack": ["Django", "Gemini AI", "SQLite"],
        "link": "https://github.com/yourusername/smart-pos-system",
        "image": None,
    },
    "afpmbai-excel-manager": {
        "title": "AFPMBAI Excel Manager",
        "subtitle": "Excel workflow management platform",
        "description": "Asset management system designed for AFPMBAI, streamlining Excel-based workflows into a web platform.",
        "stack": ["Django", "Excel", "Bootstrap"],
        "link": "https://github.com/yourusername/afpmbai-excel-manager",
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
