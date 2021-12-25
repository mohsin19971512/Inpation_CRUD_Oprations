from typing import List
from ninja import Router
from heart_surgery.models import Profile
from heart_surgery.schemas import ProfileSchemaOut

profile = Router(tags=['profile'])


@profile.get('', response=List[ProfileSchemaOut])
def list_profile(request):
    return Profile.objects.all()


