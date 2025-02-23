from django.contrib import admin
from django.urls import path, include
from tariff_dashboard import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tariff_dashboard/', include('tariff_dashboard.urls')),  
    path('', views.dashboard_view, name='home'),  
]
