from telnetlib import IP
from django.contrib import admin
from .models import IPRecord, Profile


admin.site.register(IPRecord)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type')
  
    def email(self, obj):
        return '{} {}'.format(obj.email)
 
admin.site.register(Profile, ProfileAdmin)