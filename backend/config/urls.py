from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


def health(_request):
    return JsonResponse({"status": "ok"})


public_api = [
    path("", include("apps.identity.urls")),
    path("", include("apps.tracking.urls")),
    path("", include("apps.conversations.urls")),
    path("", include("apps.pages.interfaces.urls")),
]

urlpatterns = [
    path("health/", health),
    path("admin/", admin.site.urls),
    path("api/v1/public/", include(public_api)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
