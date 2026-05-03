from django.contrib import admin
from pathlib import Path

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from salon import views as salon_views

urlpatterns = [path("admin/", admin.site.urls)]

if settings.DEBUG:
    urlpatterns += static(
        "/assets/",
        document_root=str(Path(settings.BASE_DIR).parent / "dist" / "assets"),
    )

# Catch-all: let the React router handle client-side routes.
urlpatterns += [re_path(r"^.*$", salon_views.react_app, name="react_app")]
