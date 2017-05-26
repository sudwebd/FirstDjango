from django.shortcuts import render
from django.http import Http404
from inventory.models import Item

def index(request):
    items=Item.objects.exclude(amount=0)
    return render(request,'inventory/index.html',{
        'items':items,
    })
    #return HttpResponse('<p style=\"background:rgb(0,150,200);color:white;align-content="center";size="2.5em"\">I am the index page</p>')

def item_detail(request,id):
    try:
        item=Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('The item with id {0} does not exist'.format(id))
    return render(request,'inventory/item_detail.html',{
        'item':item,
    })
    #return HttpResponse('<p style=\"background:rgb(0,150,200);color:white;align-content="center";size="2.5em"\">In item_detail view with id {0}</p>'.format(id))
