from django.contrib import admin
from prjapp.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)