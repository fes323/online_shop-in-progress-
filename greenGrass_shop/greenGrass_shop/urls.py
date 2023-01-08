from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include(('orders.urls', 'orders'), namespace='orders'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)