from django.contrib import admin
from django.urls import include,path
from django.views.generic import RedirectView
from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("sampletest/",include("sampletest.urls")),
    path('admin/', admin.site.urls),
    path("",RedirectView.as_view(url="/sampletest/")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
