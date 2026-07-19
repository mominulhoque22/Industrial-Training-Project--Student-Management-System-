from django.contrib import admin
from sciencefaculty.models import *
# Register your models here.

class StudentInline(admin.TabularInline):
    model = Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'building',
        'mission',
        'established_on'
    ]
    search_fields = ['name']
    ordering = ['name']
    inlines = [StudentInline]




@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'salary'
    ]
    search_fields = ['name', 'email']
    ordering = ['name']
    filter_horizontal = ['departments']




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'student_id',
        'name',
        'department'
    ]
    search_fields = ['name', 'student_id']
    list_filter = ['department']
    ordering = ['name']





@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'student_id',
        'subject_code',
        'marks'
    ]
    search_fields = ['student__name','student__student_id']
    list_filter = ['subject_code']
    ordering = ['marks']