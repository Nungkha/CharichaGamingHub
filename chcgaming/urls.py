from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enduser.urls')),
    path('games/', include('games.urls', namespace='games')),
    path('tournament/', include('tournament.urls', namespace='tournament')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)