from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path("contact/", views.contact, name="contact"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
]
