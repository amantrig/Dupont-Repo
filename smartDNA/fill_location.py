
from phisf.models import Verification

def set_location():
    goeLoc='17.67505645751953|78.49069213867188'
    objs=Verification.objects.filter(location='none')
    for obj in objs:
        geo_location=goeLoc
        obj.location = 'Srinagar - Kanyakumari Hwy, Telangana 501401'
        obj.save()

set_location()
