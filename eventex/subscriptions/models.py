
import hashlib
from django.db import models


def _createHash(cpf):
    return hashlib.md5(cpf.encode('utf-8')).hexdigest()


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
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
        self.hash = _createHash(self.cpf)
        super(Subscription, self).save(*args, **kwargs)