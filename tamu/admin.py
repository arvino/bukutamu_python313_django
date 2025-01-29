from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, BukuTamu

@admin.register(Member)
class MemberAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email', 'phone')
    ordering = ('-date_joined',)

@admin.register(BukuTamu)
class BukuTamuAdmin(admin.ModelAdmin):
    list_display = ('member', 'messages', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('member__username', 'messages')
    ordering = ('-timestamp',)
