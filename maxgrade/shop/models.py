from django.db import models


class Clothes(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    full_text = models.TextField('Описание')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'