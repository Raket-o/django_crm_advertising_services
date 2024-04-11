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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

from django.conf import settings
# from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap

from django.urls import path, include
# from django.conf.urls import patterns
# from django.conf.urls.defaults import
# from django.conf.urls.static import static

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from .sitemaps import sitemaps

# from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL, STATIC_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorization.urls')),
    path('statistics/', include('customer_statistics.urls')),
    path('services/', include('services.urls')),
    path('advertising-companies/', include('advertising_companies.urls')),
    # path('potential-clients/', include('potential_clients.urls')),
    path('clients/', include('clients.urls')),
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/schema/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    # path('blog/', include('blogapp.urls')),

    # path('sentry-debug/', trigger_error),

    # path(
    #     "sitemap.xml",
    #     sitemap,
    #     {"sitemaps": sitemaps},
    #     name="sitemap"
    # )
]

# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
# )

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

    # print("MEDIA_URL", settings.MEDIA_URL)
    # print("MEDIA_ROOT", settings.MEDIA_ROOT)
    # print("STATIC_URL", settings.STATIC_URL)
    # print("STATIC_ROOT", settings.STATIC_ROOT)

    # urlpatterns.append(
    #     path('__debug__/', include('debug_toolbar.urls')),
    # )