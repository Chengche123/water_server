from pyexpat import model
from django.contrib.auth.models import User
from django.db.models import Q
from water import models


def run():
    user: User = User.objects.filter(Q(username='xust'))[0]
    sensors = models.USensor.objects.all()
    for sensor in sensors:
        hx2022: models.HX2022 = models.HX2022.objects.filter(Q(code=sensor.code))[0]
        if hx2022.value == 0:
            continue
        threshold_value = hx2022.value + 1
        row = models.AlarmThreshold()
        row.user = user
        row.sensor = sensor
        row.threshold_value = threshold_value
        row.save()
