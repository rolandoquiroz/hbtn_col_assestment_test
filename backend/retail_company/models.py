from django.db import models


class User(models.Model):
    name = models.CharField(
        verbose_name='User name',
        max_length=255
        )
    last_name = models.CharField(
        verbose_name='User last name',
        max_length=255
        )
    government_issued_id = models.CharField(
        verbose_name='User government issued id',
        max_length=255
        )
    email = models.EmailField(
        verbose_name='User email',
        max_length=255
        )
    company = models.CharField(
        verbose_name='User company',
        max_length=255
        )

    # def clean(self):
    #   This method should be used to provide custom model validation,
    #   and to modify attributes on your model if desired. For instance,
    #   you could use it to automatically provide a value for a field,
    #   or to do validation that requires access to more than a single field:
    #   Cross field validation


    def get_email(self):
        return f"{self.name} has {self.email} as email."

    def __str__(self):
        return f"{self.name} {self.last_name}"
