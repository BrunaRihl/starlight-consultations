from django.contrib import admin
from booking.models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "consultant",
    ]


admin.site.register(Service, ServiceAdmin)