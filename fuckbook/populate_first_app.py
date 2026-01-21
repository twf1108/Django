import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fuckbook.settings') 

import django
django.setup()

from book1.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for _ in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()
        
        user, created = User.objects.get_or_create(
            first_name=fake_first_name, 
            last_name=fake_last_name, 
            email=fake_email
        )
        
        if created:
            print(f"Added User: {fake_first_name} {fake_last_name}, Email: {fake_email}")
        else:
            print(f"User already exists: {fake_email}")
        
if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")