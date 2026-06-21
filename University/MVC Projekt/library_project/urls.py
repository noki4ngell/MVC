from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.col_urls if hasattr(admin.site, 'col_urls') else admin.site.urls),
    path('', include('library.urls')),
]