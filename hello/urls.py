from hello import views
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('about/<str:name>', views.about),
    path('about/<str:name>/<int:age>', views.about), #/
    path('user', views.user),
    path('calculater/<int:num1>/<str:znac>/<int:num2>', views.calculater),
    path('contact', views.contact),
    path('schedule', views.schedulate),
]