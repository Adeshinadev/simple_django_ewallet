from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib import messages, auth
from .models import Wallet
from django.contrib.auth.models import User


# Create your views here.

def homepage(request):
    return render(request, 'signin.html')


def make_login(request):
    if request.method == 'POST':
        print('lloo')
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request, user)
                user_obj = User.objects.get(username=request.POST.get('username'))
                print(user_obj, 'ooooo')
                wallet_obj = Wallet.objects.filter(user=user_obj).first()

                return render(request, 'balance.html', {'wallet_obj': wallet_obj})
        messages.info(request, 'password or username incorrect')
        return render(request, 'signin.html')
    else:
        pass


def confirm_payment(request):
    user_obj = User.objects.get(id=request.POST['user_id'])
    wallet = Wallet.objects.filter(user=user_obj).first()
    a = wallet.amount
    c = a + int(request.POST['amount'])
    Wallet.objects.filter(user=user_obj).update(amount=c)
    wallet_obj = Wallet.objects.filter(user=user_obj).first()
    return render(request, 'balance.html', {'wallet_obj': wallet_obj})


def buy(request):
    user_obj = User.objects.get(id=request.user.id)
    wallet = Wallet.objects.filter(user=user_obj).first()
    a = wallet.amount
    c = a - int(request.POST['amount'])
    Wallet.objects.filter(user=user_obj).update(amount=c)
    wallet_obj = Wallet.objects.filter(user=user_obj).first()
    return render(request, 'balance.html', {'wallet_obj': wallet_obj})





