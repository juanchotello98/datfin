"""datfin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url , include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.config.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('apps.account.urls')),
    path('api/v1.0/', include('apps.budget.urls')),
    path('api/v1.0/', include('apps.category.urls')),
    path('api/v1.0/', include('apps.transaction.urls')),
    path('api/v1.0/', include('apps.user.urls')),
    url(r'^api/v1.0/auth/obtain_token/', obtain_jwt_token),
    url(r'^api/v1.0/auth/refresh_token/', refresh_jwt_token)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
