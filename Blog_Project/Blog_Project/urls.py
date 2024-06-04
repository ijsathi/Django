from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('categories/', include('categories.urls')),
    path('post/', include('post.urls')),
    path('profile/', include('profiles.urls')),
]
