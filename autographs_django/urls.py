from django.contrib import admin
from django.urls import path, include

from autographs import urls as autograph_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(autograph_urls)),
]
