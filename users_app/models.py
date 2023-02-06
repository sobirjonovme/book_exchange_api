from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework.authtoken.models import Token

KARARAKALPAKISTAN, ANDIJAN, BUKHRARA, JIZZAX, QASHQADARYO, NAVOIY, NAMANGAN,\
    SAMARKAND, SURXONDARYO, SIRDARYO, TASHKENT_CITY, TASHKENT_REGION, FERGANA, XORAZM = \
    ("Qoraqalpogʻiston", "Andijon", "Buxoro", "Jizzax", "Qashqadaryo", "Navoiy", "Namangan",
     "Samarqand", "Surxondaryo", "Sirdaryo", "Toshkent shahri", "Toshkent viloyati", "Fargʻona", "Xorazm"
     )


# Create your models here.
class CustomUser(AbstractUser):
    REGIONS = (
        (KARARAKALPAKISTAN, KARARAKALPAKISTAN), (ANDIJAN, ANDIJAN), (BUKHRARA, BUKHRARA), (JIZZAX, JIZZAX),
        (QASHQADARYO, QASHQADARYO), (NAVOIY, NAVOIY), (NAMANGAN, NAMANGAN), (SAMARKAND, SAMARKAND),
        (SURXONDARYO, SURXONDARYO), (SIRDARYO, SIRDARYO), (TASHKENT_CITY, TASHKENT_CITY),
        (TASHKENT_REGION, TASHKENT_REGION), (FERGANA, FERGANA), (XORAZM, XORAZM)
    )

    first_name = models.CharField(_("first name"), max_length=150)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="profile_images/", default='/profile_images/default_profile_pic.jpg')
    region = models.CharField(max_length=30, choices=REGIONS, default=TASHKENT_CITY)

    def get_tokens(self):
        token, created = Token.objects.get_or_create(user=self)
        data = {
            'token': token.key,
        }

        return data

    def __str__(self):
        return self.get_full_name()
