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
from core.models import Deployment
import datetime

geo_locations=['27.179306030273438|76.56778717041016',
			'26.293563842773438|75.37505340576172',
			'28.0893262|76.9749273',
			'28.10601|76.2558317',
			'27.5863599|76.075398',
			'26.82821|77.1149566',
			'26.960264205932617|76.68527221679688',
			'27.60080163948961|75.15970030231954',
			'28.3463132|76.7512992',
			'28.7874405|76.1254487']

assets=[3524600,3525600,3525500,3526700,3528200,3543600,3521600,3529600,3524900,3524200]

status_codes=[2,2,2,2,2,8,2,2,2,2]

mobile_numbers=['9636303247','9983999409','9466324873','7340602244','9784757143','9772343757',
'9466294866','9610538334','9983999409','9466683428']

bitmasks=['samsung|SM-J210F|curve|29|false|true|NA|true|true|2|3',
			'Xiaomi|Redmi 4A|curve|29|false|true|NA|true|true|2|3',
			'GiONEE|P5W|curve|29|false|true|NA|true|false|2|3',
			'samsung|SM-G610F|curve|29|false|true|NA|true|true|2|3',
			'vivo|vivo 1610|curve|29|false|true|NA|true|true|2|3',
			'Xiaomi|Redmi 3S|curve|29|false|true|NA|true|true|2|3',
			'OPPO|A1601|curve|29|false|true|NA|true|false|2|3',
			'samsung|SM-J210F|curve|29|false|true|NA|true|true|2|3',
			'samsung|SM-J210F|curve|29|false|true|NA|true|true|2|3',
			'samsung|SM-J210F|curve|29|false|true|NA|true|true|2|3']

def fill_verifications(n,start_time):
    from core.utils import getAddressElements
    from phisf.models import Verification
    from random import randint
    #'2017-06-08 08:23:33'
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%S:%M')
    record={}
    for i in range(int(n)):
        print i
        x=randint(0,9)
        asset_code='P'+str(assets[x]+i*x)
        mints=int(i*randint(0,3))
        scan_time=start_time+datetime.timedelta(minutes = mints)
        location = getAddressElements(geo_locations[x])
        print location['city']
        status=status_codes[x]
        record['asset_code']=asset_code
        record['scan_time']=scan_time
        record['credential']= '3eu3u434j2ie'
        record['d1']='0.0'
        record['d2']='0.0'
        record['d3']='0.0'
        record['h1']='0.0'
        record['h2']='0.0'
        record['h3']='0.0'
        record['angle']='5.0'
        record['orr_credential']='1000'
        record['color_profile']='nft'
        record['status']=status
        record['geo_location'] = geo_locations[x]
        record['street'] = location['street']
        record['locality'] = location['locality']
        record['city'] = location['city']
        record['state'] = location['state']
        record['postal_code'] = location['postal_code']
        record['country'] = location['country']
        record['operator']='phi_operator'
        record['auth_code'] = mobile_numbers[x]
        record['bit_mask'] = bitmasks[x]
        record['product_details']='Not provided'
        record['company_name']='Pioneer'
        record['email_id']='none'
        record['image'] = "/media/documents/signature-not-found-4.png"
        v = Verification(**record)
        v.save()

class Command(BaseCommand):
    help = 'Fill verification records'
    def add_arguments(self, parser):
        parser.add_argument('n')
        parser.add_argument('start_time')
    def handle(self, *args, **options):
        n = options['n']
        start_time = options['start_time']
        fill_verifications(n,start_time)