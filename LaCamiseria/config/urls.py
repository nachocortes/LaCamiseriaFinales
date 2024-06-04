from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.RRHH import urls as RRHHUrls
from config import views

schema_view = get_schema_view(
    openapi.Info(
        title="LaCamiseria API",
        default_version='v1',
        description="ELaCamiseria API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="ilarranaga@egibide.org"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', include('core.LOGIN.urls')),
    path('', include('core.STORE.urls')),
    path('ventas/', include('core.VENTAS.urls')),
    path('index/', views.index, name='index'),
    path('api/', include(RRHHUrls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
