from django.contrib import admin
from . import models

admin.site.register(models.SkillSet)
admin.site.register(models.JobPostSkillSet)
admin.site.register(models.JobType)

admin.site.register(models.JobPost)
admin.site.register(models.Company)
admin.site.register(models.CompanyBusinessArea)
admin.site.register(models.BusinessArea)
admin.site.register(models.JobPostActivity)
admin.site.register(models.JobPostActivityStatus)
admin.site.register(models.JobPostActivityStatusChange)