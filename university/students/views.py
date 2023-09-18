from random import randint

import faker
from django.shortcuts import render

from .models import Student


def generate_student(request):
    f = faker.Faker()
    student = Student.objects.create(
        first_name=f.first_name(),
        last_name=f.first_name(),
        age=randint(1, 100)
    )
    return render(request, 'student.html', {'student': student})


def generate_students(request):
    count = request.GET.get('count')
    if count is None:
        return render(request, 'generate_students_error.html', {'message': 'Please provide a count parameter.'})
    try:
        count = int(count)
        if not 0 < count <= 100:
            return render(request, 'generate_students_error.html', {'message': 'Count should be between 1 and 100.'})
    except ValueError:
        return render(request, 'generate_students_error.html', {'message': 'Invalid count parameter.'})

    fake = faker.Faker()
    students = []
    for _ in range(count):
        student = Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=randint(1, 100)
        )
        students.append(student)

    return render(request, 'students.html', {'students': students})
