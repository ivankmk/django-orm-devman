import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    passcards = Passcard.objects.all()
    passcard = passcards[2]

    print({'owner_name':  passcard.owner_name,
           'passcode': passcard.passcode,
           'created_at': passcard.created_at,
           'is_active': passcard.is_active})
