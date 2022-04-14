from telnetlib import IP
from django.contrib import admin
from .models import CustomUser, IPRecord, Profile


admin.site.register(IPRecord)
admin.site.register(Profile)


# class CustomUserInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = False
#     verbose_name_plural = 'User'


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('get_email', 'user_type')
#     can_delete = False
#     inlines = (CustomUserInline,)

#     def get_email(self, obj):
#         return '{}'.format(obj.user.email)
 
# admin.site.register(Profile, ProfileAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type')
    can_delete = False
    inlines = (ProfileInline,)

    def user_type(self, obj):
        return '{}'.format(obj.profile.user_type)

admin.site.register(CustomUser, CustomUserAdmin)
