"""
URL configuration for homesecurity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login,name="index"),
    path('', views.index,name="home"), 
    path('logout/',views.logout_view,name='logout') ,
    path('sensor-data/', views.display_sensor_data, name='sensor-data'),
    path('smoke-data-report/', views.smoke_data_report, name='smoke_data_report'),
    path('human-data-report/', views.human_data_report, name='human_data_report'),
    path('object-data-report/', views.object_data_report, name='object_data_report'),
]
