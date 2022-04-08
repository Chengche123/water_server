from django.urls import path, include

urlpatterns = [
    path('', include('water.urls')),
]
