from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
app_name = 'cofee_m'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coffe_m.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
