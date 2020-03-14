from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilizador


@receiver(post_save, sender=Utilizador)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Utilizador.objects.create(user=instance)


@receiver(post_save, sender=Utilizador)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()