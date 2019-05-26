from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from . import forms
from AppTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            #DO SOMETHING LANGUAGE_CODE
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'AppTwo/user.html',{'form':form})
