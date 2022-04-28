from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from water import views

router = DefaultRouter()
router.register(r'hx2021', views.HX2021ViewSet)
router.register(r'hx2022', views.HX2022ViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'sensors', views.USensorViewSet)
router.register(r'alarm-threshold', views.AlarmThresholdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('rest_framework.urls')),
    path('user', views.user),
    path('admin/', admin.site.urls),
]
