from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/', include('orders.urls'), name='orders'),
    path('cart/', include('cart.urls'), name='cart'),
    path('shop/', include('shop.urls'), name="shop"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)