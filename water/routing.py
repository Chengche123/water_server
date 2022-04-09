from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r"^ws/hx2022-consumer/$", consumers.HX2022Consumer.as_asgi()),
]
