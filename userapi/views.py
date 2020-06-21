from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import User,RegisterForm,LoginForm
from django.http import HttpResponse
import json
from django.contrib import auth
from .validators_users import ValidateEmail




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            gender = form.cleaned_data.get('gender')
            status = True
            error = None
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                     status = False
                     error = "Такой адресс электронной почты уже существует!"

            if User.objects.filter(username=username).exists():
                status = False
                error = "Имя пользователя существует!"
            
            email_val = ValidateEmail(form.cleaned_data.get('email'))

            if email_val == False:
                status = False
                error = "Проверьте правильность ввода email !"
                
    
            if (password1 != password2) or (password2 != password1):
                status = False
                error = "Password is not validate!"

            if status == True:
                User.objects.create_user(username=username, email=form.cleaned_data.get('email'), date_of_birth=date_of_birth,gender=gender)
                user=User.objects.get(email=form.cleaned_data.get('email'))
                user.set_password(password1)
                user.save()

            dict_user = json.dumps({
            "error": error,
            "status": status,
            })
            return HttpResponse(dict_user, content_type="application/json")
        else:
            return HttpResponse("Не все поля введены!")
    return HttpResponse("Другие методы не разрешены!")


def login_user(request):
     if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                token_key = Token.objects.get(user_id=user.id)
                dict_user = json.dumps({
                    "username" :user.username,
                    "email" :user.email,
                    "date_of_birth":user.date_of_birth,
                    "gender":user.gender,
                    "token_key": token_key.key,
                    })

                return HttpResponse(dict_user,content_type="application/json")
            else:
                return HttpResponse("Что то пошло не так :( Проверьте введенные данные!")
        return HttpResponse("Неверное количество полей!")








