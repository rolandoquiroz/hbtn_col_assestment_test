from django.contrib import admin
from retail_company.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
