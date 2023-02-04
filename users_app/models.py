from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework.authtoken.models import Token


# Create your models here.
class CustomUser(AbstractUser):

    first_name = models.CharField(_("first name"), max_length=150)

    def get_tokens(self):
        token, created = Token.objects.get_or_create(user=self)
        data = {
            'token': token.key,
        }

        return data
