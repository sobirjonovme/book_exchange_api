from django.contrib import admin

from users_app.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
