from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from users.validators import is_alphanumeric
from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True
        )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        blank=True
        )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=255,
        blank=True
        )
    gov_id = models.CharField(
        verbose_name=_('government issued id'),
        max_length=255,
        blank=True,
        validators=[is_alphanumeric]
        )
    company = models.CharField(
        verbose_name=_('company'),
        max_length=255,
        blank=True
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # def clean(self):
    #   This method should be used to provide custom model validation,
    #   and to modify attributes on your model if desired. For instance,
    #   you could use it to automatically provide a value for a field,
    #   or to do validation that requires access to more than a single field:
    #   Cross field validation

    '''
    def get_email(self):
        return f"user identified with {self.id} id has {self.email} as email."
    '''
    def __str__(self):
        return f"{self.email}"
