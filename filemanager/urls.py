from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('files:file_list')),  # Redirect root to file list with namespace
    path('files/', include('files.urls')),  # Include our app URLs with prefix
    path('', include('django.contrib.auth.urls')),  # Include authentication URLs
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
