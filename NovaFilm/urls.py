from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', include('Home.urls')),
    path('profile/', include('users.urls')),
    path('api/', include('api.urls')),
    path('', include('admin_soft.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)