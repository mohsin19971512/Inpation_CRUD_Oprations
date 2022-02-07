from typing import List
from django.contrib.auth import get_user_model
from ninja import Router
from pydantic.types import UUID4
from heart_surgery.models import  Profile
from account.authorization import GlobalAuth
from .schemas import MessageOut, ProfileNameSchemaOut,ProfileSchemaIn,ProfileSchemaOut
from django.shortcuts import get_object_or_404
from django.db.models import Q

User = get_user_model()
profile = Router(tags=['profile'])


@profile.post('create_profile/', auth=GlobalAuth(),response={201:MessageOut,404:MessageOut})
def create_profile(request,profile_input:ProfileSchemaIn):
    user = get_object_or_404(User,id=request.auth['pk'])
    profile = Profile(**(profile_input.dict()),added_by = user)
    profile.save()

    return 201,{"message":"created successfully"}


@profile.put('get_profile_to_update/{id}/', response={404:MessageOut,200:MessageOut})
def update_profile(request,id,update_profile:ProfileSchemaIn):
    profile = get_object_or_404(Profile,id=id)
    for attr, value in update_profile.dict().items():
        setattr(profile, attr, value)
    
    profile.save()
    return 200,{"message":"Profile Updated Successfully"}


@profile.get('get_profile_details/{id}/', response={404:MessageOut,200:ProfileSchemaOut})
def details(request,id):

    profile = get_object_or_404(Profile,id=id)
 
    return 200,profile



@profile.delete('delete_profile/{id}/', response={404:MessageOut,200:MessageOut})
def delete(request,id):
    profile = get_object_or_404(Profile,id=id)
    profile.delete()
    
    return 200,{'message':'Profile Deleted Successfully'}



@profile.get('get_all_names/', response={404:MessageOut,200:List[ProfileNameSchemaOut]})
def list_names(request):
    return Profile.objects.all()



@profile.get('get_all_profile/', auth=GlobalAuth(), response={404:MessageOut,200:List[ProfileSchemaOut]})
def get_all_profile(request):
    profile = Profile.objects.all()
    if not profile:
        return 404, {'message': 'No profile found'}
    return 200,Profile.objects.all()



@profile.get('search_to/', response={404:MessageOut,200:List[ProfileNameSchemaOut]})
def search_to(request,search:str = None):
    profile = Profile.objects.all()
    if not profile:
        return 404, {'message': 'No profile found'}
    if search :
        profile = profile.filter(
            Q(name__icontains=search) | Q(age__icontains=search)| Q(diagnoses__icontains=search)|
            Q(Bed__icontains=search)| Q(Ward__icontains=search)| Q(number__icontains=search)|
            Q(gender__icontains=search) |Q(operation_type__icontains=search)|
            Q(entry_date_time__icontains=search)|Q(operation_date_time__icontains=search)|
            Q(leaving_date_time__icontains=search)|Q(medications__icontains=search) 
        )     

    return 200,profile

