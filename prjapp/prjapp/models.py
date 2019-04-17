from django.db import models

class Project(models.Model):
	project_id=models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	start_date = models.CharField(max_length=8)
	end_date=models.CharField(max_length=8)
	def __str__(self):
		return self.name
	