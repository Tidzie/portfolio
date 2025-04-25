from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Election, Candidate, Vote

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role', 'is_staff')
    list_select_related = ('userprofile',)

    def get_role(self, instance):
        return instance.userprofile.role
    get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'election_type', 'start_date', 'end_date', 'status', 'candidate_count', 'total_votes')
    list_filter = ('status', 'election_type')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at', 'updated_at', 'status')
    inlines = [CandidateInline]
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        # If the election is already created, don't allow changing election_type
        if obj and obj.pk:
            readonly_fields.append('election_type')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'election')
    list_filter = ('election__status', 'election__election_type')
    search_fields = ('user__username', 'user__email', 'election__title')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'candidate', 'timestamp')
    list_filter = ('candidate__election',)
    search_fields = ('user__username', 'candidate__user__username', 'candidate__election__title')
    date_hierarchy = 'timestamp'
    readonly_fields = ('user', 'candidate', 'timestamp')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
