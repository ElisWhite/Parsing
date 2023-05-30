from django.urls import path, re_path
from django.views.generic import TemplateView
from parser_cafe import views

urlpatterns = [
 path('', views.index, name='index'),
 path('cafe/<path:link>', views.cafe, name='cafe'),
]
