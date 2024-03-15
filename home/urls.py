from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from .views import home
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [ 
    path('', home, name="home"), 
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)