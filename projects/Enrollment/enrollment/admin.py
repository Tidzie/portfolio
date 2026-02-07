from django.contrib import admin
from .models import Parent, Child, Enrollment

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'parent', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'parent__user__username')
    list_filter = ('date_of_birth',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('child', 'class_type', 'enrollment_date', 'status')
    list_filter = ('class_type', 'status', 'enrollment_date')
    search_fields = ('child__first_name', 'child__last_name', 'child__parent__user__username')
