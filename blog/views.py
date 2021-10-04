from django.shortcuts import render
from django.http import HttpResponse
from .forms import AccountForm


# Create your views here.


def index(request):
    return HttpResponse('my weblog address : www.cafedeep.ir')


def UserAccount(request):
    if request.method == 'POST':
        form = AccountForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountForm()
    return render(request, 'blog/forms/account-form.html', {'form': form})

