from django.core.management.base import BaseCommand
from faker import Faker
from company.models import Department, Employee, Attendance, Performance
import random

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        dept_names = ['Engineering', 'HR', 'Marketing', 'Sales']
        departments = [Department.objects.get_or_create(name=n)[0] for n in dept_names]

        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-3y', end_date='today'),
                department=random.choice(departments)
            )
            for _ in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date='-1y', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )
            for _ in range(3):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS('Database seeded.'))
