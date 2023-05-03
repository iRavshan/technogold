from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import Home, Contact, About, Services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', Home, name='home'),
    path('contact', Contact, name='contact'),
    path('about', About, name='about'),
    path('services', Services, name='services')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
