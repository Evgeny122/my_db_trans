from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import News
 

# def index(request):
#     return render(request, 'base/index.html')

# def query(request, pk):
#     context = {'pk': pk}
#     print(pk)
#     return render(request, 'base/query.html', context)

def start_news(request):
    an = News.objects.all()
    context = {'all_news' : an}
    return render(request, 'base/query.html', context)

def detail(request, pk):
    obj = News.objects.get(id=pk)
    return render(request, 'base/detail.html', {'text': obj})
    



