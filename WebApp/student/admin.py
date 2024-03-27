from django.contrib import admin
from . models import CourseInfo,BatchInfo,StudentInfo

# Register your models here.
admin.site.register(CourseInfo)
admin.site.register(BatchInfo)
admin.site.register(StudentInfo)
