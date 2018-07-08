from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'phone')
    search_fields = ['email']

admin.site.register(Member, MemberAdmin)