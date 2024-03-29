from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from .views import *
from django.conf import settings
from django.conf.urls.static import static
  
app_name = 'home'

urlpatterns = [ 
    path('', home,name='homepage'), 
    path('chat', chatBot, name="chatbot"), 
    path('releases', pressReleases, name="release"), 
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)