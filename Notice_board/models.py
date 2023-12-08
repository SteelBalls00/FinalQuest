import os

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='имя')
    email_confirmed = models.BooleanField(default=False)


# Функция для генерации пути сохранения изображений
def user_image_path(instance, filename):
    username = instance.user.user.username
    return os.path.join('images', username, filename)

def user_video_path(instance, filename):
    username = instance.user.user.username
    return os.path.join('video', username, filename)

class Category(models.Model):

    tank = 'Tank'
    hiller = 'Hiller'
    dd = 'DD'
    merchants = 'Merchants'
    guildmasters = 'Guildmasters'
    questgivers = 'Questgivers'
    blacksmiths = 'Blacksmiths'
    tanners = 'Tanners'
    potions_brewers = 'Potions_brewers'
    spell_masters = 'Spell_masters'

    CATEGORY_TYPES = [
        (tank, 'Танк'),
        (hiller, 'Хиллер'),
        (dd, 'Дамаг диллер'),
        (merchants, 'Торговец'),
        (guildmasters, 'Гилдмастер'),
        (questgivers, 'Квестгивер'),
        (blacksmiths, 'Кузнец'),
        (tanners, 'Кожевник'),
        (potions_brewers, 'Зельевар'),
        (spell_masters, 'Мастер заклинаний'),
    ]

    name = models.CharField(max_length=72, choices=CATEGORY_TYPES, default=tank, verbose_name='Категория объявления')

    def __str__(self):
        return self.name

class Announcement(models.Model):


    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Автор', related_name='Announcement_user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Announcement_category')
    title = models.CharField(max_length=72, default="Пустой заголовок", verbose_name='Заголовок')
    content = models.TextField(max_length=4048, default='', verbose_name='Контент', help_text='текст подсказки')
    image = models.ImageField(upload_to=user_image_path, null=True, blank=True)
    video = models.FileField(upload_to=user_video_path, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}: {self.content[:10]}'

    def get_absolute_url(self):
        return reverse('Notice_board:announcement_detail', args=[str(self.id)])


class Response(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='Response_announcement')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Response_user')
    content = models.TextField(max_length=4048, default='', help_text='текст отлкика')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика')
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Reaction on {self.user}\'s {self.announcement}'

class SubscribedUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)