from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("sampletest",include("sampletest.urls")),
    path('admin/', admin.site.urls),
]
