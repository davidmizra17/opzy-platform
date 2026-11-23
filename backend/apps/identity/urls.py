from django.urls import path

from .views import StartSessionView

urlpatterns = [path("visitors", StartSessionView.as_view(), name="start-session")]
