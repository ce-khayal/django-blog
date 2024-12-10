from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.
def index(request):  # HttpReguest  
    return HttpResponse("<h2>khayal tətbiqinin səhifəsi<h2>")

def about(request):  # HttpReguest  
    return HttpResponse("haqqimizda")

def contact(request):  # HttpReguest  
    return HttpResponse("elaqe:05000000000")

def categories(request, name, age): 
    return HttpResponse(f""" 
            <h2>Kateqoriyalar üzrə məqaləler</h2> 
            <p>Name: {name}</p> 
            <p>Age: {age}</p> 
        """)

def user(request, name, age): 
    return HttpResponse(f"<h2>Name: {name} Age: {age}</h2>")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h3>Axtardiginiz melumat teesuf ki yoxdur</h3>')

def user1(request):
    age=request.GET.get('age', 0)
    name=request.GET.get('name', "Yoxdur")
    return HttpResponse(f'<h2>Name:{name} age:{age}</h2>')

menu = ["Sayt haqqında", "Məqalənin əlavə olunması", "Əlaqə", "Daxil olmaq"]

def sablon(request):
    data={'title':'Esas seyfe','header':'Basliq', 'message':'xos geldin dostum :)', 'menu':menu}
    return render(request,'khayal/index.html',context=data)

def sablon2(request):
    return render(request,'khayal/about.html')

def yeni(request):
    data={
        'list': ['rəqəmlər', 'sətirlər', 'siyahılar', 'kortejlər', 'lüğətlər'],
        'int': 123,
        'str':'dsds',
        'tupl' : {12,13,14},
        'ds' :{'lex12','six12'},

    }
    return render(request,"khayal/about.html",context=data)
