"""
URL configuration for django_crm project.

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

from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter

from services.views import ServiceViewSet
from advertising_companies.views import AdvertisingCompanyViewSet
from clients.views import ClientViewSet, ClientActiveViewSet, ClientToActiveViewSet
from contracts.views import ContractViewSet

routers = DefaultRouter()
routers.register("services", ServiceViewSet, basename='services')
routers.register("advertising-companies", AdvertisingCompanyViewSet, basename='advertising_companies')
routers.register("clients", ClientViewSet, basename='clients')
routers.register("client-to-active", ClientToActiveViewSet, basename='client_to_active')
routers.register("client-active", ClientActiveViewSet, basename='client_active')
routers.register("contracts", ContractViewSet, basename='contracts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorization.urls')),
    path('statistics/', include('customer_statistics.urls')),
    path('services/', include('services.urls')),
    path('advertising-companies/', include('advertising_companies.urls')),
    path('clients/', include('clients.urls')),
    path('contracts/', include('contracts.urls')),

    path("api/", include(routers.urls)),

    # path('api/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

    urlpatterns.append(
        path('__debug__/', include('debug_toolbar.urls')),
    )

    urlpatterns += staticfiles_urlpatterns()
