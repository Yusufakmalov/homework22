from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Django1 import settings
from items.views import home
from products.views import index_page, ShopPageView, send_form



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('', ShopPageView),
    path('form', send_form),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)