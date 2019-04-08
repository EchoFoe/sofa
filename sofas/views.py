from django.shortcuts import render
from sofas.models import *


def sofa(request, sofa_id):
    sofas = Sofa.objects.get(id=sofa_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'sofas/sofa.html', locals())