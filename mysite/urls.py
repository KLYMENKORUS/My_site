from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"", include("blog.urls", namespace="blog")),
    path("users/", include("users.urls", namespace="users")),
    path("social-auth/", include("social_django.urls", namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
