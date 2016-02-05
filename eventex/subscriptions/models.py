
import hashlib
from django.db import models
from django.shortcuts import resolve_url as r
from eventex.subscriptions.validators import validate_cpf


def _createhash(cpf):
    return hashlib.md5(cpf.encode('utf-8')).hexdigest()


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    hash = models.CharField(max_length=32, unique=True)
    paid = models.BooleanField('Pago', default=False)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.hash = _createhash(self.cpf)
        super(Subscription, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return r('subscriptions:detail', self.pk)
