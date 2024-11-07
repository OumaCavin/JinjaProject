from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

]