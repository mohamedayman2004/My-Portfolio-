from django.contrib import admin
from .models import Profile, Project, Experience, Skill, ProjectCategory, Certificate

admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(ProjectCategory)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'category', 'date_earned')
    list_filter = ('category', 'issuer')
    search_fields = ('title', 'issuer', 'description')
    ordering = ('-date_earned',)