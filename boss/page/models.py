from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Call(models.Model):
    date = models.DateTimeField(
        verbose_name='Дата',
        blank=True,
        null=True,
        help_text='Дата',
    )
    full_name = models.TextField(
        max_length=70,
        verbose_name='ФИО Организация Должность',
        help_text='ФИО Организация Должность'
    )
    question = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Вопрос',
        help_text='Суть вопроса'
    )
    telephone = models.TextField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Телефон'
    )
    result = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Итог',
        help_text='Итог'
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'

    def __str__(self):
        return f'{self.full_name} {self.question} {self.telephone} {self.result}'
    

class Birthday(models.Model):
    full_name = models.TextField(
        max_length=100,
        verbose_name='ФИО',
        help_text='ФИО'
    )
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения',
        help_text='Дата рождения'
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'дни рождения'

    def __str__(self):
        return f'{self.full_name} {self.date}'


class Reception(models.Model):
    full_name = models.TextField(
        max_length=100,
        verbose_name='ФИО',
        help_text='ФИО'
    )
    question = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Вопрос',
        help_text='Вопрос'
    )
    other = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Дополнительно',
        help_text='Дополнительно'
    )
    class Meta:
        verbose_name = 'посещение'
        verbose_name_plural = 'посещения'

    def __str__(self):
        return f'{self.full_name} {self.other}'
