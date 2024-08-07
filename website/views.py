from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,QueryDict
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.
def index_views (request):
    return render(request,'website/index.html')
def about_views (request):
    return render(request,'website/about.html')
def contact_views (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_name = form.save(commit=False)
            new_name.name = "Unknown"
            new_name.save()
            form.save_m2m()
           
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submitted')
        
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})
        

def test_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form=ContactForm()
    return render(request,'test.html',{'form':form})


