from django.contrib import admin
from django.urls import path, include
#from django.views.generic.base import TemplateView
from django.conf.urls.static import static  # This is for serving static files
from django.conf import settings
from . import views

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('admin/', admin.site.urls),  TURNING THIS OFF FOR SECURITY
    path('admin_vsj/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('skiing/', include('skiing.urls')),
    path('reading/', include('reading.urls')),
    path('french/', include('french.urls')),
    path('techstuff/', include('techstuff.urls')),
    path('sensors', include('sensors.urls')),
    path('wordcount', include('wordcount.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#print("===URLPATTERNS=== ", urlpatterns)
