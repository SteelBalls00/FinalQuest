from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.models import EmailConfirmation
from django.contrib.auth.models import Group

from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from Project import settings
from Notice_board.models import Response, SubscribedUsers
from protect.models import NewsToSend


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


def send_email_notif(response, title, template, subscribers_email):
    #берет за основу шаблон и создает текст письма
    html_mail = render_to_string(
        template,
        {
            'text': response,
        }
    )

    message = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_email
    )

    message.attach_alternative(html_mail, 'text/html')
    message.send()


@receiver(post_save, sender=Response)
def new_reply_added(sender, instance, **kwargs):
    if kwargs['created'] == True:
        send_email_notif(instance.announcement, f'Новый отклик на обьявление {instance.announcement.title}', 'reply_add_email.html', [instance.user.email])

@receiver(post_save, sender=Response)
def reply_accepted(sender, instance, **kwargs):
    if kwargs['update_fields'] == {'accepted'}:
        send_email_notif(instance.announcement, f'Ваш отклик принят. Обьявление: {instance.announcement.title}', 'reply_add_email.html', [instance.user.email])

@receiver(post_save, sender=NewsToSend)
def send_news(sender, instance, **kwargs):
    #Если не черновик - то рассылаем новости
    if not instance.is_draft:
        subscribers = set(SubscribedUsers.objects.all())
        subscribers_emails = []
        for sub_users in subscribers:
            subscribers_emails.append(sub_users.user.email)
        send_email_notif(instance.wysiwyn_text, f'{instance.title}',
                     'protect/news_subscribe.html', subscribers_emails)