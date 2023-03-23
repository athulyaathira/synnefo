from django.contrib import admin
from.models import *

# Register your models here.
class display_department(admin.ModelAdmin):
  list_display=['dep_name']
class display_batch(admin.ModelAdmin):
  list_display=['batch_time']
class display_student(admin.ModelAdmin):
  list_display=['std_name','Address','dept']
admin.site.register(Department,display_department)
admin.site.register(Batch,display_batch)
admin.site.register(student,display_student)





