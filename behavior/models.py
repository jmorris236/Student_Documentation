from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class StudentNote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Note for {self.student} on {self.created_at}'
