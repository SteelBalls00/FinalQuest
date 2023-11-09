from django.db.models.signals import pre_delete
from django.dispatch import receiver

from Notice_board.models import Announcement

# Удаление файлов из media вместе с объявлением при его удалении
@receiver(pre_delete, sender=Announcement)
def delete_announcement_media(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
    if instance.video:
        instance.video.delete(save=False)


# @receiver(user_signed_up)
# def send_welcome_email(request, user, **kwargs):
#     subject = 'Добро пожаловать!'
#     message = render_to_string('subscribe/welcome_email.html', {
#         'user': user,
#     })
#     user.email_user(subject, message)