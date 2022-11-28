from django.db.models.signals import pre_save
from django.dispatch import receiver
from api.models import Gym,Sink,Paddle,Futbol,Reserbas


@receiver([pre_save],sender=Reserbas)
def increment_users(sender,**kwargs):#,sender:Reserbas):#created,raw,using,update_fields):
    FIELDS = ("gym","pileta","futbol","paddle")
    print("-->",kwargs.get("update_fields"))
    print("-->|||",kwargs)
    if FIELDS[0] or FIELDS[1] or FIELDS[2] or FIELDS[3] in update_fields:
        obj = None
        
        if sender.pileta:
            obj = sender.pileta
        elif sender.futbol:
            obj = sender.futbol
        elif sender.gym:
            obj = sender.gym
        else:
            obj = sender.paddle
        
        if obj.limit_users == obj.maximum_capacity:
            obj.has_capacity = False
            obj.save(update_fields=["has_capacity"])
        else:
            obj.limit_users += 1
            obj.save(update_fields=["limit_users"])
