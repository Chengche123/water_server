import random
import string
from water.models import HX2022, USensor


choice = random.SystemRandom().choice
def random_username(N): return ''.join(choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(N))


def validated_sensor_and_value():
    all_sensors: list[USensor] = USensor.objects.all()
    validated_sensors = []
    for sensor in all_sensors:
        code = sensor.code
        hx2022s = HX2022.objects.filter(code=code)
        if not hx2022s:
            continue
        hx2022: HX2022 = hx2022s[0]
        if hx2022.value == 0:
            continue
        validated_sensors.append([sensor, hx2022.value])
    return validated_sensors
