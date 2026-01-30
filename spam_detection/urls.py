from django.urls import path
from .views import home, detect

urlpatterns = [
    path("", home, name="home"),
    path("detect/", detect, name="detect"),
]
