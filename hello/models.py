from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField( max_length=18)
    email = models.EmailField()
    psw = models.CharField(max_length=20)
    phone = models.CharField( max_length=13)
    age = models.IntegerField()
    brd = models.DateField(auto_now=True)
#django-admin startproject name_of_project
#python manage.py startapp name_app
#python manage.py runserver
#python manage.py makemigrations
#python manage.py migrate
"""
filter()
exclude()
order_by()
distinct()
value()
value_list()
all()
get()
create()
update()
delete()
first()
last()
exists()
contains()
"""