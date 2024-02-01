from django.shortcuts import render
from django.http import HttpResponse

from app.forms import *

# Create your views here.

# def insert_topic(request):
#     ETFO=Topicform()
#     d={'ETFO':ETFO}

#     if request.method == 'POST':
#         TFDO=Topicform(request.POST)
#         if TFDO.is_valid():
#             TFDO.save()
#             return HttpResponse('Topic Modelform is created')

#     return render(request,'insert_topic.html',d)

# def insert_webpage(request):
#     EWFO=Webpageform()
#     d={'EWFO':EWFO}

#     if request.method == 'POST':
#         WFDO=Webpageform(request.POST)
#         if WFDO.is_valid():
#             WFDO.save()
#             return HttpResponse('WebPage Modelform is created')

#     return render(request,'insert_webpage.html',d)

# def insert_accessrecord(request):
#     EAFO=Accessrecordform()
#     d={'EAFO':EAFO}
#     if request.method == 'POST':
#         AFDO=Accessrecordform(request.POST)
#         if AFDO.is_valid():
#             AFDO.save()
#             return HttpResponse('AccessRecord Modelform is created')
    
#     return render(request,'insert_accessrecord.html',d)



def djforms(request):
    ENFO=NameForm()
    d={'ENFO':ENFO}

    if request.method=='POST':
        NFDO=NameForm(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
            #return HttpResponse(NFDO.cleaned_data['Sname'])
        else:
            return HttpResponse('Data is not Valid')
    return render(request,'djforms.html',d)


