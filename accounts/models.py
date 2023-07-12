from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.utils import generate_partner_token
from django.db.models.signals import post_save


# Create your models here.


class User(AbstractUser):
    pass


class Partner(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=230, null=True)
    is_guest = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    json_text = models.TextField(null=True, blank=True)
    token = models.IntegerField(max_length=6, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    class Meta:
        verbose_name_plural = 'partner'


def partner_created(sender, **kwargs):
    ins = kwargs['instance']
    if kwargs['created']:
        token = generate_partner_token()
        ins.token = token
        ins.save()

    # else:
    #
    #     if not ins.itnumber:
    #         itnumber = increment_it_number(code)
    #         ins.itnumber = itnumber
    #         ins.save()


post_save.connect(partner_created, Partner)
