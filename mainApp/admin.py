from django.contrib import admin

# Register your models here.
from mainApp.models import *

admin.site.register(MyUser)
admin.site.register(Klass)
admin.site.register(Student)
admin.site.register(Problem)
admin.site.register(Examination)
admin.site.register(ExaminationProblem)
admin.site.register(Answer)
admin.site.register(Grade)
