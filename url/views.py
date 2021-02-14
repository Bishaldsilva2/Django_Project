from django.shortcuts import render,redirect
from django.contrib import messages
import random,string,uuid
from .models import link
# Create your views here.
def home(request):
    return render(request,'url/index.html')
def short(request):
    df=link.objects.values('url','uuid')
    l=[i['url'] for i in df]
    lnk=request.POST['address']
    if lnk not in l:
        uid = str(uuid.uuid4())[:5]
        new_link=link(url=lnk,uuid=uid)
        new_link.save()
        messages.info(request,"http://127.0.0.1:8000/"+uid)
    else:
        row=link.objects.get(url=lnk)
        messages.info(request,"http://127.0.0.1:8000/"+row.uuid)
    return redirect('/')
def go(request, pk):
    url_details =link.objects.get(uuid=pk)
    print(url_details)
    return redirect(url_details.url)

