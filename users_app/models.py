from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator

from rest_framework.authtoken.models import Token

KARARAKALPAKISTAN, ANDIJAN, BUKHRARA, JIZZAX, QASHQADARYO, NAVOIY, NAMANGAN,\
    SAMARKAND, SURXONDARYO, SIRDARYO, TASHKENT_CITY, TASHKENT_REGION, FERGANA, XORAZM = \
    ("Karakalpakistan", "Andijan", "Bukhara", "Djizzak", "Kashkadarya", "Navoi", "Namangan",
     "Samarkand", "Surkhandarya", "Syrdarya", "Tashkent", "Tashkent province", "Fergana", "Khorezm"
     )


# Create your models here.
class CustomUser(AbstractUser):
    REGIONS = (
        (KARARAKALPAKISTAN, KARARAKALPAKISTAN), (ANDIJAN, ANDIJAN), (BUKHRARA, BUKHRARA), (JIZZAX, JIZZAX),
        (QASHQADARYO, QASHQADARYO), (NAVOIY, NAVOIY), (NAMANGAN, NAMANGAN), (SAMARKAND, SAMARKAND),
        (SURXONDARYO, SURXONDARYO), (SIRDARYO, SIRDARYO), (TASHKENT_CITY, TASHKENT_CITY),
        (TASHKENT_REGION, TASHKENT_REGION), (FERGANA, FERGANA), (XORAZM, XORAZM)
    )

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[
            username_validator,
            MinLengthValidator(5, message="Username should be 5 characters at least")
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
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
        return self.username

    def clean(self):

        existing_usernames = CustomUser.objects.filter(username__iexact=self.username).exclude(pk=self.pk)

        if existing_usernames.exists():
            raise ValidationError({
                'username': _("A user with that username already exists."),
            })
