from datetime import datetime
import requests
from requests import auth
import time
from water.models import HX2021, HX2022, USensor
from water.serializers import HX2022Serializer
from django.db.models import Q

LOGIN_URL = 'http://127.0.0.1:8000/users/login'
POST_URL = 'http://127.0.0.1:8000/hx2022/'
LOGIN_USERNAME = 'xust'
LOGIN_PASSWORD = 'xust'


def run():
    sensors = USensor.objects.all()
    for sensor in sensors:
        sensor_code = sensor.code
        hx2021s = HX2021.objects.filter(code__exact=sensor_code)[:100]
        for hx2021 in hx2021s:
            hx2022: HX2022 = HX2022()
            hx2022.value = hx2021.value
            hx2022.code = hx2021.code
            hx2022.save()


"""
1. ` pip install django-extensions `
2. ` python manage.py runscript test `
"""
