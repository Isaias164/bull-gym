from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Gym,Sink,Paddle,Futbol,Reserbas


# @receiver(post_save,sender=Reserbas)
# def increment_users(sender,**kwargs):#,instance,created,raw,using,update_fields):
#     instance = kwargs.get("instance")
#     created = kwargs.get("created")
#     if created:
#         #print(instance.pk)
#         FIELDS = ("gym","pileta","futbol","paddle")
#         if FIELDS[0] or FIELDS[1] or FIELDS[2] or FIELDS[3] in update_fields:
#             obj = None
            
#             c = sender.objects.get(pk=instance.pk)
#             print(kwargs)
            
#             if instance.pileta:
#                 print("cayo en pileta")
#                 obj = instance.pileta
#             elif instance.futbol:
#                 print("cayo en futbol")
#                 obj = instance.futbol
#             elif instance.gym:
#                 print("cayo en gym")
#                 obj = instance.gym
#             elif instance.paddle:
#                 print("cayo en paddle")
#                 obj = instance.paddle
            
            
