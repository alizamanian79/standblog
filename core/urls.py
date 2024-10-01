
from django.urls import include  
from django.contrib import admin  
from django.urls import path  

from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', include('website.urls')), 
    path('accounts/',include('accounts.urls')) ,
    path('blog/', include('blog.urls')),  
    path('captcha/', include('captcha.urls')),
]  

# Serve static files in development  
if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)