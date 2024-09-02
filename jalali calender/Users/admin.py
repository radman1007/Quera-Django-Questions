from Users.models import CustomUser
from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender', 'national_code', 'jbirthday_date']
    search_fields = ['username', 'full_name']
    ordering = ('ceremony_datetime',)

    @admin.display(description='تاریخ')
    def jbirthday_date(self, obj):
        return datetime2jalali(obj.birthday_date)