from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
   


class Department(TimeStampedModel):
    name = models.CharField(max_length=100)
    building= models.CharField(max_length=40)
    mission = models.TextField()
    established_on = models.DateField()
    def __str__(self):
        return self.name


class Teacher(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    departments = models.ManyToManyField(Department,related_name='teachers')
    def __str__(self):
        return self.name



class Student(TimeStampedModel):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name="students"
        )
    def __str__(self):
        return self.name


class Result(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject_code = models.CharField(max_length=100)
    marks = models.FloatField(
        validators=[MinValueValidator(0,message="Marks must be 0 or greater"), MaxValueValidator(100,message="Marks must be 100 or less")]
    )
    class Meta:
        unique_together = ('student', 'subject_code')
    def __str__(self):
        return f"{self.student.name} - {self.subject_code}"



class DepartmentHead(TimeStampedModel):
    department = models.OneToOneField(
        Department, 
        on_delete=models.CASCADE,
        related_name="head" 
    )
    teacher = models.OneToOneField(
        Teacher, 
        on_delete=models.CASCADE,
        related_name="head_of_department"
    )
    



