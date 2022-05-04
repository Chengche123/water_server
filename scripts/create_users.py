import random
import requests
from requests import auth
from . import api, utils
from water import models


def run():
    sensor_and_values = utils.validated_sensor_and_value()

    for _ in range(10):
        random_str = utils.random_username(4)
        r = requests.post(api.USERS_URL, json={
            'username': random_str,
            'password': random_str,
        })

        # 可能用户名已存在
        try:
            r.raise_for_status()
        except:
            continue

        user_id = r.json()['id']

        for sensor_and_value in sensor_and_values:
            sensor, value = sensor_and_value

            m: models.AlarmThreshold = models.AlarmThreshold()
            m.user_id = user_id
            m.sensor_id = sensor.autoid
            m.method = random.choice([0, 1, 2, 4, 3, 5, 6, 7])

            m.threshold_value_max = value + random.random()
            threshold_value_min = value - random.random()
            if threshold_value_min < 0:
                threshold_value_min = 0
            m.threshold_value_min = threshold_value_min

            m.save()
