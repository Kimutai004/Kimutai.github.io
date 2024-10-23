# portfolio/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Ensure this points to your index view
]

if settings.DEBUG:  # Serve media files during development only
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)