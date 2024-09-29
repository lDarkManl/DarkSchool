from django.contrib import admin
from accounts.models import TeacherAccount, StudentAccount, User

admin.site.register(TeacherAccount)
admin.site.register(StudentAccount)
admin.site.register(User)
# Register your models here.
