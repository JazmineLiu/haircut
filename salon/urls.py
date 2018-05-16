from django.urls import include, path 
from django.contrib import admin

urlpatterns = [ 
     path('', include('haircut.urls')), 
     path('admin/', admin.site.urls),
]
