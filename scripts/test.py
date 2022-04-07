from water.models import HX2021


def run():
    qs = HX2021.objects.all()
    print(qs[:10])


"""
1. ` pip install django-extensions `
2. ` python manage.py runscript test `
"""
