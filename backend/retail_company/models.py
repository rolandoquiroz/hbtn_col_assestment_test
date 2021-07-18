from django.db import models
from django.core.validators import MinLengthValidator, validate_email


class User(models.Model):
    name = models.CharField(
        verbose_name='User name',
        max_length=255, validators=[MinLengthValidator(2)])
    last_name = models.CharField(
        verbose_name='User last name',
        max_length=255,
        validators=[MinLengthValidator(2)])
    government_issued_id = models.CharField(
        verbose_name='User government issued id',
        max_length=255, unique=True)
    email = models.EmailField(
        verbose_name='User email',
        max_length=255, unique=True,
        validators=[validate_email])
    company = models.CharField(
        verbose_name='User company',
        max_length=255,
        blank=True,
        default="")

    def __str__(self):
        return f"{self.name} {self.last_name}"
