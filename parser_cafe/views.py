from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Cafe

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.template.response import TemplateResponse

start_url = "https://ua.igotoworld.com/ru/poi_object/"

def get_soup(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    return soup

def cafe(request, link):
    #url = request.GET.get('cafe')
    url = start_url+link+'.htm'
    print("YRL",url)
    soup = get_soup(url)
    info = soup.find('div', class_='tour-description-text').findAll('p')
    info1 = soup.find('div', class_='tour-description-text').findAll('div')
    

    text = []
    if len(info)>0:
        for i in info:
            text.append(i.text)
        print(text)
    else:
        for i in info1:
            text.append(i.text)
    img = soup.find('div', class_='poi-image-holder').find('img').get('src')
    name = soup.find('div', class_='poi-title-block').find('h1').text
    print("TEXT",text)
    print(img)
    print(name)

    data = {'cafe':Cafe(name=name, img=img, info=text, adress='', link='#')}
    return TemplateResponse(request, 'cafe.html', context=data)

def index(request):
    url = "https://ua.igotoworld.com/ru/poi_catalog/6-9-cafe-ukraine.htm"

    soup = get_soup(url)

    info = soup.findAll('div', class_='newsListItem')
    img = []
    name = []
    link = []
    adress = []
    text = []
    for a in info:

        img.append(a.find('div', class_='newsListItemImage').find('img')['src'])
        url = a.find('div', class_='newsListItemImage').find("a")['href']
        urls = url.split("/")[-1].split(".")[0]
        link.append(urls)
        name.append(a.find('div', class_='newsListItemText newsListItemTextShort').find('a').text)
        adress.append(a.find('div', class_='newsListItemIcons newsListItemTextAddress').text)
        text.append(a.find('div', class_='newsListItemTextDescription').text)

    all = []
    for i in range(len(img)):
        cafe = Cafe()
        cafe.link = link[i]
        cafe.img = img[i]
        cafe.name = name[i]
        cafe.adress = adress[i]
        cafe.info = text[i]
        all.append(cafe)
    print(all[0].name, all[-1].name)
    date = {"cafe": all}
    return TemplateResponse(request, 'index_cafe.html', context=date)

