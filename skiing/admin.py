from django.contrib import admin

from .models import Resort
from .models import SkiDay
from django.contrib import admin


class SkiDayInLine(admin.TabularInline):
    model = SkiDay
    extra = 0


class ResortAdmin(admin.ModelAdmin):
    inlines = [SkiDayInLine, ]


# Register your models here.
admin.site.register(Resort, ResortAdmin)
admin.site.register(SkiDay)

admin.ModelAdmin.list_per_page = 1000


