from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.contrib.auth.models import Group


from Notice_board.models import Announcement

# Удаление файлов из media вместе с объявлением при его удалении
@receiver(pre_delete, sender=Announcement)
def delete_announcement_media(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
    if instance.video:
        instance.video.delete(save=False)

@receiver(post_save, sender=EmailConfirmation)
def assign_email_confirmed_group(sender, instance, created, **kwargs):
    if created:
        email_address = instance.email_address
        user = email_address.user
        group, _ = Group.objects.get_or_create(name='email_confirmed')
        user.groups.add(group)

# @receiver(user_signed_up)
# def send_welcome_email(request, user, **kwargs):
#     subject = 'Добро пожаловать!'
#     message = render_to_string('subscribe/welcome_email.html', {
#         'user': user,
#     })
#     user.email_user(subject, message)