from django.contrib import admin

from .models import Group
from Teachers.models import Teacher
from students.models import Student


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", )
    inlines = [TeacherInline, StudentInline]
