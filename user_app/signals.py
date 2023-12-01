from .models import CustomUser, Code
from django.dispatch import receiver
from django.db.models.signals import post_save
from .sms import SendSMS


@receiver(post_save, sender=CustomUser)
def create_code(sender, instance, created, **kwargs):
    if created:
        Code.objects.create(user=instance)

        # Send SMS with verification code
        send_sms = SendSMS(recipient=instance.phone_number, code=instance.code.code)
        send_sms.sending(instance.username)
