# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from nusxchange.models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )     
    #overriding the list_display attribute.
    list_display = ('username', 'is_staff', 'get_accomodation', 'get_school', 'title') 

    list_select_related = ('profile', )

    def title(self,instance):
        return instance.profile.title
        
    def get_accomodation(self, instance):
        return instance.profile.accomodation
    get_accomodation.short_description = 'Accomodation'

    def get_school(self, instance):
        return instance.profile.school
    get_school.short_description = 'School'


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

