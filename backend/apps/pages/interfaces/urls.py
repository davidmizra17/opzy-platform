from django.urls import path

from .views import PageView, RevertPageView

urlpatterns = [
    path("pages/<uuid:page_id>", PageView.as_view(), name="page-detail"),
    path("pages/<uuid:page_id>/revert", RevertPageView.as_view(), name="page-revert"),
]
