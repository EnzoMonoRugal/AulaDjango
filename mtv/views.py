from django.shortcuts import render
from .models import Access, Page, Topic
from .forms import *


def topic_view(req):
    title = 'Topic'
    identifier = 'name'
    data = Topic.objects.all()

    render_data = {
        "title": title,
        "identifier": identifier,
        "data": data
    }

    return render(req, 'mtv/base_list.html', render_data)

    
def access_view(req):
    title = 'Access'
    identifier = 'page'
    data = Access.objects.all()

    render_data = {
        "title": title,
        "identifier": identifier,
        "data": data
    }

    return render(req, 'mtv/base_list.html', render_data)


def page_view(req):
    title = 'Page'
    identifier = 'name'
    data = Page.objects.all()   

    render_data = {
        "title": title,
        "identifier": identifier,
        "data": data
    }

    return render(req, 'mtv/base_list.html', render_data)

def home(request):
    return render(request, 'mtv/home.html',)

def index(request):
    return render(request,'mtv/base_list.html')

def match(request):
    return render(request,'mtv/index.html')


def cadastrar_usuario(request):
    form=UsuarioForm
    mydict={
        'form':form
    }
    if request.method == "POST":
        form=UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
        return render(request,'mtv/form.html',{'data':form.cleaned_data})
    else:
        form = UsuarioForm()
    return render(request, "mtv/form.html", context=mydict)



