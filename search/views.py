from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.core import serializers
from .models import Store
import json
import api_engine


def index(request):
    return render(request, 'search/index.html')

def login(request):
    return render(request, 'search/login.html')

def select(request):
    t = request.POST.get('title')
    book = api_engine.bookInfo(t)
    if not book:
        return render(request, 'search/nobook.html')
    context = {'b': book, 't': t}
    return render(request, 'search/select.html', context)


def result(request, isbn):
    i = str(isbn)
    stock = api_engine.getStock(i)
    n = 0
    # DB에 각 지점 재고 업데이트 위한 for문
    for i in stock.values():
        n += 1 # pk 위한 변수
        # 재고를 받아올 때 지점 순서와 DB에 입력된 지점 순서는 동일
        # db에 입력된 지점의 pk는 1씩 늘어남
        # pk를 기준으로 지점을 순서대로 받아와 해당 지점에 재고 업데이트
        q = Store.objects.filter(pk=n).update(stock=int(i))
    #seoul = serializers.serialize('json', Store.objects.filter(in_seoul=True).order_by('-stock'), ensure_ascii=False)
    #not_seoul = serializers.serialize('json', Store.objects.filter(in_seoul=False).order_by('-stock'), ensure_ascii=False)
    s = Store.objects.filter(in_seoul=True).order_by('-stock')
    ns = Store.objects.filter(in_seoul=False).order_by('-stock')
    seoul = [Store.dict() for Store in s]
    not_seoul = [Store.dict() for Store in ns]

    context = {'in_seoul': seoul, 'not_seoul': not_seoul }
    return render(request, 'search/result.html',context)
   