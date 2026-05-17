from django.contrib import admin
from .models import Profile, Technology, Project, Experience, Education, Testimonial, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'location')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'profile_image', 'about_image', 'resume')
        }),
        ('Bio Story', {
            'fields': ('hero_title', 'hero_subtitle', 'bio_short', 'bio_detailed')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'instagram_url', 'behance_url')
        }),
        ('SEO Meta Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        # Allow only one profile configuration instance
        if self.model.objects.exists():
            return False
        return True


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'featured', 'order')
    list_editable = ('proficiency', 'featured', 'order')
    list_filter = ('category', 'featured')
    search_fields = ('name',)
    ordering = ('category', 'order', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'order', 'created_at')
    list_editable = ('featured', 'order')
    list_filter = ('featured', 'technologies')
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    date_hierarchy = 'created_at'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'current', 'order')
    list_editable = ('current', 'order')
    list_filter = ('current', 'company')
    search_fields = ('role', 'company', 'description')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('degree', 'institution', 'field_of_study')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_title', 'project_relation', 'order')
    list_editable = ('order',)
    search_fields = ('client_name', 'client_title', 'quote')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected messages marked as read.")
    mark_as_read.short_description = "Mark selected messages as Read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, "Selected messages marked as unread.")
    mark_as_unread.short_description = "Mark selected messages as Unread"
