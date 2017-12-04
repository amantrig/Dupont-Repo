import os
import sys
import json
import time
os.environ['PYTHON_EGG_CACHE'] = "/tmp"
PROJECT_PATH=os.path.dirname(os.path.realpath(__file__)).split("smartDNA")[0]
FILE_PATH=PROJECT_PATH+"smartDNA"
path = PROJECT_PATH+'smartDNA/'
if path not in sys.path:
    sys.path.append(path)
path = PROJECT_PATH
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'smartDNA.settings'

from django.core.management.base import BaseCommand, CommandError
from core.models import Deployment

def fill_location():
    from core.utils import getAddressElements
    from django.db.models.loading import get_model
    q=Deployment.objects.values('dep_path').distinct()
    for index in range(q.count()):
     dep_path=q[index]['dep_path']
     Verification = get_model(dep_path, 'Verification')
     objs=Verification.objects.filter(city='none',status__in=[2,3,4,5,8,12]).order_by('-scan_time').exclude(geo_location='0.0|0.0')
     total= objs.count()
     print total
     for obj in objs:
        time.sleep(1.0)
        l=getAddressElements(str(obj.geo_location))
        print l['city']
        obj.street=l['street']
        obj.locality=l['locality']
        obj.city=l['city']
        obj.state=l['state']
        obj.postal_code=l['postal_code']
        obj.country=l['country']
        obj.save()
     print str(total)+' locations filled'
    return total

class Command(BaseCommand):
    help = 'Fill location every 15 minutes'
    def handle(self, *args, **options):
        fill_location()
