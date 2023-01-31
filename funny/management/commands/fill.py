from django.core.management import BaseCommand

from funny.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        students = [
            {'first_name': 'Олег', 'last_name': 'Маслов'},
            {'first_name': 'Никита', 'last_name': 'Евсюков'},
            {'first_name': 'Дима', 'last_name': 'Екименков'},
            {'first_name': 'Дима', 'last_name': 'Саушкин'},
        ]

        student_list = []
        for item in students:
            # student_list.append(Student(first_name=item['first_name'], last_name=item['last_name']))
            student_list.append(
                Student(**item)
            )
            # student.save()

            # Student.objects.create(first_name=item['first_name'], last_name=item['last_name'])
        Student.objects.bulk_create(student_list)
