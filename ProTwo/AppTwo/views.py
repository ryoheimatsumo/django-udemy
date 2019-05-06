from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App<em>")


def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users':users_list}
    return render(request, 'AppTwo/user.html', context=user_dict)
