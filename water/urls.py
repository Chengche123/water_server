from django.urls import path, include

from rest_framework.routers import DefaultRouter

from water import views

router = DefaultRouter()
router.register(r'hx2021', views.HX2021ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
