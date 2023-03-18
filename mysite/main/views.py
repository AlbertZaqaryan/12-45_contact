from django.shortcuts import render, redirect
from .models import Phone, Contact
from .forms import ContactForm
# Create your views here.

def home(request):
    phone_list = Phone.objects.all()
    return render(request, 'main/home.html', context={
        'phone_list':phone_list
    })


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', context={
        'form':form
    })