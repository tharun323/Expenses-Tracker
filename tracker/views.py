from django.shortcuts import render,redirect,reverse

from django.shortcuts import get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect

from .forms import ItemModelForm

from . models import Item

from django.db.models import Sum

import re,json

def add_item(request):
    k=Item.objects.aggregate(Sum('price'))
    l=json.dumps(k)
    p=re.findall("\d+",l)
    item = Item.objects.all()
    if request.method == "POST":
        form = ItemModelForm(request.POST,request.FILES)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            form = ItemModelForm()
            return HttpResponseRedirect('/item')
            #return render(request,"tracker/display.html")
    else:
        form = ItemModelForm()
    return render(request, "tracker/index.html", {'form': form ,'item':item,'sum':p })


def update(request,id):
    instance=get_object_or_404(Item,id=id)
    form=ItemModelForm(data=request.POST, files=request.FILES, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
        "name":instance.name,
        "price":instance.price,
        "instance":instance,
        "form":form,
    }
    return render(request,"tracker/update.html",context)





def delete(request,id):
    deleteitem=get_object_or_404(Item,pk=id).delete()
    return HttpResponseRedirect('/item')

def sortbyname(request):
    sname=Item.objects.order_by('name').all()
    return render(request,"tracker/sname.html",{'name':sname})


def sortbyprice(request):
    sprice=Item.objects.order_by('price').all()
    return render(request,"tracker/sprice.html",{'price':sprice})

def sortbydate(request):
    sdate=Item.objects.order_by('created_at').all()
    return render(request,"tracker/sdate.html",{'date':sdate})
