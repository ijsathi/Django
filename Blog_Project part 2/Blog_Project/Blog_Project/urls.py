from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('', include('author.urls')),
    path('categories/', include('categories.urls')),
    path('post/', include('post.urls')),
]
