from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('items/', include('item.urls')),
    path('orders/', include('orders.urls')),
     path('api/', include('item.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
