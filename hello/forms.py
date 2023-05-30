from django import forms

class UserForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, strip=True, empty_value="Enter name", label="Enter name", initial="John",help_text="Enter name")
    age = forms.IntegerField()
    email = forms.EmailField()
    male = forms.BooleanField()
    m = forms.NullBooleanField()
    ip = forms.GenericIPAddressField()
    slug = forms.SlugField(required=False, empty_value="qwerty")
    #combo= forms.ComboField(fields=[name, age])
    file = forms.FileField()
    image = forms.ImageField()
    date = forms.DateField()
    textarea = forms.CharField(widget=forms.widgets.FileInput)
    field_order = ["name", "email", "age", "male", "ip", "m", "slug", "date", "textarea", "image", "file"]

class Register(forms.Form):
    name = forms.CharField(min_length=3, max_length=18, strip=True)
    email = forms.EmailField()
    psw = forms.CharField()
    phone = forms.CharField(min_length=10, max_length=13)
    age = forms.IntegerField(min_value=14)
    brd = forms.DateField()

