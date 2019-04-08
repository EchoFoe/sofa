from django.shortcuts import render
from about_us.models import *


def about_us(request, about_id):
    about = About_us.objects.get(id=about_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'abouts_us/about_us.html', locals())