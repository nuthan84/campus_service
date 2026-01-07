from django.contrib import admin
from .models import Complaint
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'assigned_staff',
        'status',
        'created_at'
    )
    list_filter = ('status',)
    search_fields = ('title', 'user__username')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        staff_users = User.objects.filter(profile__role='STAFF')
        form.base_fields['assigned_staff'].queryset = staff_users
        return form
