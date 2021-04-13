from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

admin.site.site_header = 'Administration Matrice des compétences AOOMUKI'


# class UserAdmin(admin.ModelAdmin):
#     pass

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ( 'last_name', 'first_name','email', 'is_staff', 'is_superuser', 'is_collaborater', 'society','date_joined' )
    list_filter = ('society', 'is_collaborater', 'is_superuser')

    fieldsets = (
        (None, {'fields': (  'last_name', 'first_name','email', 'is_staff', 'is_superuser', 'is_collaborater', 'society','date_joined' )}),
       
    )
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {
    #         'classes': ('wide', ),
    #         'fields': ( 'last_name', 'first_name','email', 'is_staff', 'is_superuser', 'is_collaborater', 'society' )
    #     }),
    # )
    # search_fields = ('last_name', 'first_name', 'society',)
    # ordering = ('last_name', )


admin.site.register(User, UserAdmin)

