from django.contrib import admin
from django.urls import path
from movies import views


urlpatterns = [
    path("admin/", admin.site.urls),

    # Home page
    path("", views.home, name="home"),

    # Movie pages
    path("bahubali/", views.bahubali, name="bahubali"),
    path("pushpa/", views.pushpa, name="pushpa"),
    path("rrr/", views.rrr, name="rrr"),
    path("salaar/", views.salaar, name="salaar"),
    path("kgf/", views.kgf, name="kgf"),
    path("vikram/", views.vikram, name="vikram"),
    path("leo/", views.leo, name="leo"),
    path("jailer/", views.jailer, name="jailer"),
    path("devara/", views.devara, name="devara"),
    path("kalki/", views.kalki, name="kalki"),
]