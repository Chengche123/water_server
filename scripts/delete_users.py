from django.contrib.auth.models import User
from django.db.models import Q


def run():
    users = User.objects.exclude(username__in=['xust'])
    users.delete()
