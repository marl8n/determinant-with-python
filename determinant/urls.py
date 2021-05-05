"""determinant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# Views
from determinant import views as determinant_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('3x3/', determinant_views.calculate_determinat3x3, name="calculate3x3"),
    path('4x4/', determinant_views.calculate_determinat4x4, name="calculate4x4"),
]
