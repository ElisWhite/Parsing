from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.template.response import TemplateResponse
from .forms import UserForm, Register
from .models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f'<h2> Hello, {name}! You are age {age}</n2>')
    else:
        header = "Information of user"
        langs = ["Python", "Java", "C#"]
        user = {"name": "Tom", "age": 23}
        address = ("Bayker Street", 23, 45)
        userform = UserForm()
        data = {"header": header, "langs": [], "user": user, "address": address, "message":"Welcome to Python", "form": userform}
        return render(request, "index_cafe.html", context=data)

def about(request, name="Undefined", age=0):
    header = "Information of user"
    langs = ["Python", "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    address = ("Bayker Street", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return TemplateResponse(request, "about.html", data)

def user(request):
    age = request.GET.get('age')
    name = request.GET.get('name')
    lang = request.GET.get('lang')
    return HttpResponse(f'<h2>NAME: {name}, Age: {age}, {lang}</h2>')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        psw = request.POST.get("psw")
        user = User()
        user.name = name
        user.age = age
        user.email = email
        user.phone = phone
        user.psw = psw
        #User.objects.create(name=name, age=age, email=email, phone=phone, psw=psw)
        #user.save()
        usr = []
        try:

            john = User.objects.get(name="John")

            print(john)

        except MultipleObjectsReturned:
            john = User()
            print("Multi")
        except ObjectDoesNotExist:
            john = User()
            print("NotExist")
           # john.save()
        usr.append(john)
        users = User.objects.all()
        user.save()
       # us = users.filter(name="sdsdf")
        usrs = User.objects.all()
        data = {'user': user, "users": users}
        return  TemplateResponse(request, "about.html", data)
    else:
        reg = Register()


        data = {"form": reg}
        return TemplateResponse(request, "contact.html", data)
     #header = "Information of user"
     #langs = ["Python", "Java", "C#"]
     #user = {"name": "Tom", "age": 23}
     #address = ("Bayker Street", 23, 45)
     #data = {"header": header, "langs": langs, "user": user, "address": address}
     #return TemplateResponse(request, "contact.html", data)


def calculater(request, num1, znac, num2):
    if znac == "+":
        rez=num1+num2
    elif znac == "-":
        rez=num1-num2
    elif znac=="*":
        rez=num1*num2
    elif znac=="/":
        rez=num1/num2
    return HttpResponse(f'''
        <h2> Your result is {rez}!</h2>
''')

def schedulate(request):
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]
    day1 = ["Укр мова", "Хімія", "Праця", "Алгебра", "Фізика", "Зар літ", "Фізра", '']
    day3 = ["Укр мова", "Історія", "Історія", "Біологія", "Географія", "Інформ", "Фізра",""]
    day4 = ["ЗВ", "Гаометрія", "Гром освіта", "Укр літ", "Фізика", "Англ мова", "Укр КВ",""]
    day5 = ["-", "Історія", "Історія", "Біологія", "Фізра", "Гром освіта", "Інформ",""]
    day2 = ["Історія", "Історія", "фізика", "Англ мова", "Географія", "Геометрія", "Укр літ", "ЗВ"]
    lessons = {days[0]:day1, days[1]:day2, days[2]:day3, days[3]:day4, days[4]:day5}
    data = {'lessons': lessons, 'text': 'Hello', 't':" Django"}
    print(data)
    return render(request, "schedule.html", context=data)


#cd ./Caramel
#python manage.py runserver