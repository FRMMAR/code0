from django.shortcuts import render
from django.http import HttpResponse
from movieSpider import savedata
from m1.models import M1Models

# Create your views here.

def index(request,page=1):
#    return render(request, 'movie.html', context={'title':M1Models.objects.get(id=55).title})
    page=int(page)
    if page > 1:
        return render(request, 'movie.html', context={'model_list':M1Models.objects.all()[(page-1)*15:page*15],'up':page+1})
    else:
        return render(request, 'movie.html', context={'model_list':M1Models.objects.all()[:15],'up':page+1})
    
def movie_page(request, id):
    model = M1Models.objects.get(id=id)
    return render(request, 'content.html', context={'title': model.title, 'content': model.content,'link': model.link})
    
def up(request, page_num):
    page_num = int(page_num)
    savedata(page_num)
    return HttpResponse('ok')
