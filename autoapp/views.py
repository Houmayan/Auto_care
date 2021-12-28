from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from Auto_care import settings
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def showroom(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        msg = request.POST['msg']
        to = request.POST['email']
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER,[to,'183002312@eastdelta.edu.bd',
                                                                '183000412@eastdelta.edu.bd',
                                                                '183001512@eastdelta.edu.bd'])

        if res:
            return HttpResponse("Email send")
        else:
            return HttpResponse("Email not send")
    return render(request, 'showroom_form.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Please Enter the correct Password or Username')
            return redirect('autoapp:login')
    else:
        return render(request, 'login.html')


# aka sign_up
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect('autoapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect('autoapp:register')

            else:

                user = User.objects.create_user(username=username, \
                                                email=email, password=password1, \
                                                first_name=first_name, \
                                                last_name=last_name)

                user.save()
                print("user created")
                return redirect("autoapp:login")
        else:
            print("password didn't match")
        return redirect('/')
    else:

        return render(request, 'sign-up.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def treading(request):
    return render(request, 'treading.html')
