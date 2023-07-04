from django.shortcuts import render

from sayt.models import Subscribe


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "index.html", ctx)