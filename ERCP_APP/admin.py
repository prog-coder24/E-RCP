from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

from .forms import *

# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email',)
    fieldsets = (
        ('Personal Information', {
         'fields': ('email','is_staff', 'is_active')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    readonly_fields = ( 'email',)
    search_fields = ('email',)
    ordering = ('email',)

class CardDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_name','roll_no',)

class FormDetailsAdmin(admin.ModelAdmin):
    list_display = ('railway_class','duration',)

admin.site.register(User, UserAdmin)
admin.site.register(CardDetails, CardDetailsAdmin)
admin.site.register(FormDetails, FormDetailsAdmin)

