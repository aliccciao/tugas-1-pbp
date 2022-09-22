from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

def main(request):
    return render(request, "main.html")

def show_watchlist(request):
    my_watchlist = MyWatchList.objects.all()

    context = {
        'data': my_watchlist,
        'nama': 'Alicia Kirana Utomo',
        'id': '2106751505'
    }
    
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")