from django.db.models.signals import pre_delete, post_delete
from .models import Rent
from django.dispatch import receiver


@receiver(pre_delete, sender=Rent)
def pre_delete_rent(sender, instance, **kwargs):
    obj = instance.vehicle
    obj.status = 1
    obj.save()
