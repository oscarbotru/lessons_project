from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        (STATUS_ACTIVE, 'активный'),
        (STATUS_INACTIVE, 'отчислен')
    )

    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')

    email = models.CharField(max_length=50, verbose_name='Email', **NULLABLE)  # , unique=True)

    status = models.CharField(choices=STATUSES, default=STATUS_ACTIVE, max_length=10)

    # register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
