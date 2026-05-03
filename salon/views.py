from pathlib import Path

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def react_app(request):
    """
    Serve the existing Vite build output (dist/index.html) so the Django server
    shows the original frontend instead of a placeholder template.
    """
    index_path = Path(settings.BASE_DIR).parent / "dist" / "index.html"
    try:
        html = index_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return HttpResponseNotFound(
            "Frontend build not found at dist/index.html. Run `npm run build`."
        )

    return HttpResponse(html, content_type="text/html; charset=utf-8")
