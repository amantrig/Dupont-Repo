import os
import sys
import json
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
from core.models import Deployment,Logger
import datetime
from core.models import Configuration

days=7 #get_expiry_days()

def deleteVerificationMedia():
    from django.db.models.loading import get_model
    q=Deployment.objects.values('dep_path').distinct()
    for index in range(q.count()):
     dep_path=q[index]['dep_path']
     Verification = get_model(dep_path, 'Verification')
     v=Verification.objects.filter(scan_time__lt=datetime.datetime.now()-datetime.timedelta(days=int(days))).exclude(status=1)
     print v.count()," image records of verification deleted successfuly"
     for item in v:
        image=item.image
        if os.path.isfile(FILE_PATH+image.name) and image!="/media/documents/signature-not-found-4.png":
          os.remove(FILE_PATH+image.name)
     

def deletePostmortemMedia():
    from django.db.models.loading import get_model
    q=Deployment.objects.values('dep_path').distinct()
    for index in range(q.count()):
     dep_path=q[index]['dep_path']
     PostmortemImage = get_model(dep_path, 'PostmortemImage')
     p=PostmortemImage.objects.filter(scan_time__lt=datetime.datetime.now()-datetime.timedelta(days=int(days)))
     print p.count()," image records of postmortem deleted successfuly"
     for item in p:
        image=item.imagefile
        if os.path.isfile(FILE_PATH+image.name):
          os.remove(FILE_PATH+image.name)

class Command(BaseCommand):
    help = 'Delete all the rocords which are older than 7 days'
    def handle(self, *args, **options):
        deleteVerificationMedia()
        deletePostmortemMedia()
