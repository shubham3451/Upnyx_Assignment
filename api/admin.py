from django.contrib import admin
from .models import Chat, User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

@admin.register(Chat)
class chatAdmin(admin.ModelAdmin):
    list_display = ('user','message', 'response', 'timestamp',)
