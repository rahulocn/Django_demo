from tastypie.resources import ModelResource
from tastypie.constants import ALL

from prjapp.models import Project


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'prjapp'
        filtering = {'name': ALL}