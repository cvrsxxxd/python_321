from django.shortcuts import render, redirect

from PopkaMladencaApp.models import CustomUser


# Create your views here.

def custom_registration(request):
    return render(request, 'register.html')


# Проверка введенных данных
def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        mail = request.POST.get('mail')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        number = request.POST.get('phone_number')
        adress = request.POST.get('adress')

        if password1 != password2:
            return redirect('/register/')

        CustomUser(first_name=first_name, email=mail, password=password1,
                   phone_number=number, username=number, adress=adress).save()

        return redirect(('/register'))
