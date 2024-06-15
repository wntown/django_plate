from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['username', 'name', 'useremail', 'phone',
                    'is_active', 'is_admin', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'uuid']
    search_fields = ('username', 'name', 'uuid',)
    readonly_fields = ('last_login', 'date_joined', 'uuid',)  

    filter_horizontal = ()
    list_filter = (
        'is_active',
        ('date_joined', DateRangeFilter),
        )
    #list_per_page = 1
    fieldsets = ()

    

admin.site.register(Account, AccountAdmin)