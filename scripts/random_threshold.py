import random
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
        threshold_value_max = hx2022.value + 1
        threshold_value_min = hx2022.value - 1
        if threshold_value_min < 0:
            threshold_value_min = 0

        row = models.AlarmThreshold()
        row.user = user
        row.sensor = sensor
        row.threshold_value_min = threshold_value_min
        row.threshold_value_max = threshold_value_max
        row.method = random.choice([0, 1, 2, 4, 3, 5, 6, 7])
        row.save()
