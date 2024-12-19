from django.contrib import admin

from .models import Call, Birthday, Reception


@admin.register(Call, Birthday, Reception)
class CallAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = 'BOSS BOARD'
admin.site.index_title = 'админка'