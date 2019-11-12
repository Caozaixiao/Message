from django.contrib import admin
from .models import *

admin.site.site_title = '留言板后台管理'
admin.site.site_header = '留言板后台'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'message']
