from django.shortcuts import render
from .forms import *
from sofas.models import *
from about_us.models import *
from guarantees.models import *
from contacts.models import *

def home(request):
    sofas_images = SofaImage.objects.filter(is_active=True, is_main=True, Sofa__is_active=True)
    sofas_images_1 = sofas_images.filter(Sofa__category__id=1)


    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'landing/home.html', locals())

def contacts(request):
    contact = Contacts.objects.get(id=1)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'contacts/contacts.html', locals())


def abouts_us(request):
    about = About_us.objects.get(id=1)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'abouts_us/about_us.html', locals())


def guarantees(request):
    guarantee = Guarantees.objects.get(id=1)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'guarantees/guarantees.html', locals())