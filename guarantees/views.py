from django.shortcuts import render
from guarantees.models import *


def guarantees(request, guarantee_id):
    guarantee = Guarantees.objects.get(id=guarantee_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'guarantees/guarantees.html', locals())