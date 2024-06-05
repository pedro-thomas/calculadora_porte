"""
URL configuration for calculadora_porte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from calculadora.views import register_sale, sale_list, calculate_totals, sale_report


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-sale/', register_sale, name='register_sale'),
    path('sale-list/', sale_list, name='sale_list'),
    path('calculate-totals/', calculate_totals, name='calculate_totals'),
    path('sale-report/<int:sale_id>/', sale_report, name='sale_report'),
]
