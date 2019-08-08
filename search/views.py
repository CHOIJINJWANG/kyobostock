from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import api_engine

def index(request):
    return render(request,'search/index.html')

def select(request):
    t = request.POST.get('title')
    if t == '':
        return render(request,'search/nobook.html')
    book = api_engine.bookInfo(t)
    print(book)
    if book == []:
        return render(request,'search/nobook.html')
    context = {'b': book}
    return render(request, 'search/select.html', context)

def result(request, isbn):
    #i = request.POST.get('isbn')
    i = str(isbn)
    stock = api_engine.getStock(i)
    context = {'stock': stock}
    return render(request, 'search/result.html', context)