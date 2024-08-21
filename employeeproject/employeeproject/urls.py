from django.contrib import admin
from django.urls import path, include  # include is used to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),  # Include app1 URLs
]
