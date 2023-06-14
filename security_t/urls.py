from django.urls import path

from . import views

urlpatterns = [
    path("xss_t/", views.xss_t, name="xss_t"),
    path("csrf_t/", views.csrf_t, name="csrf_t"),
    path("cors_t/", views.cors_t, name="cors_t"),
    path("sqlinject_t/", views.sqlinject_t, name="sqlinject_t"),
]
