from datetime import datetime
import requests
from requests import auth
import time
from water.models import HX2021, HX2022, USensor
from water.serializers import HX2022Serializer

LOGIN_URL = 'http://127.0.0.1:8000/users/login'
POST_URL = 'http://127.0.0.1:8000/hx2022/'
LOGIN_USERNAME = 'xust'
LOGIN_PASSWORD = 'xust'


def run():
    # sensors = USensor.objects.filter(sensortypename__exact='温度')
    # sensor = sensors[1]
    # code = sensor.code
    code = 37501207308501

    s = requests.Session()
    r = s.get(LOGIN_URL, auth=auth.HTTPBasicAuth(LOGIN_USERNAME, LOGIN_PASSWORD))
    r.raise_for_status()

    # post test
    r = s.post(POST_URL, json={})
    r.raise_for_status()

    hx2021s = HX2021.objects.filter(code__exact=code)
    count = hx2021s.count()
    inx = 0
    inc = 100
    while inx + inc <= count:
        inx += inc
        for hx2021 in hx2021s[inx:inx + inc]:
            hx2021: HX2021 = hx2021

            hx2022: HX2022 = HX2022()
            hx2022.value = hx2021.value
            hx2022.code = hx2021.code
            hx2022.udatetime = datetime.now()
            hx2022_json = HX2022Serializer(hx2022).data

            print(hx2022_json)
            r = s.post(POST_URL, json=hx2022_json)
            r.raise_for_status()

            time.sleep(2)


"""
1. ` pip install django-extensions `
2. ` python manage.py runscript test `
"""
