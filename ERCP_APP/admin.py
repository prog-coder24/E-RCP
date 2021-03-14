from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .forms import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field

# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','date_joined','has_card')
    list_filter = ('email',)
    fieldsets = (
        ('Personal Information', {
         'fields': ('email','is_staff', 'is_active','date_joined','has_card')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    
    search_fields = ('email',)
    ordering = ('date_joined',)

class CardDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_name','roll_no','residential_addr',)
    readonly_fields = ('journey_to',)

class FDResource(resources.ModelResource):
    Name = Field()
    journey_from = Field()
    via = Field()

    class Meta:
        model = FormDetail
        fields = ('railway_class', 'duration', 'issue_date')

    def dehydrate_Name(self, FormDetail):
        return FormDetail.user_card.user_name
    
    def dehydrate_journey_from(self, FormDetail):
        return FormDetail.user_card.journey_from
    
    def dehydrate_via(self, FormDetail):
        return FormDetail.user_card.via


class FormDetailsAdmin(ImportExportModelAdmin):
     resource_class = FDResource
     list_display = ('Name','journey_from','via','railway_class','duration','issue_date','status')
     list_filter = ('applied_date',)
     ordering = ('applied_date',)

     def Name(self, obj):
        return obj.user_card.user_name
     def journey_from(self, obj):
        return obj.user_card.journey_from
     def via(self, obj):
        return obj.user_card.via
     


admin.site.register(User, UserAdmin)
admin.site.register(CardDetail, CardDetailsAdmin)
admin.site.register(FormDetail, FormDetailsAdmin)
admin.site.unregister(Group)

