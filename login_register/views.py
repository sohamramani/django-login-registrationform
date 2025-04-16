import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django_countries import countries
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token


def deactivate_user(user_id):
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        return True
    except User.DoesNotExist:
        return False

def home(request):
    return render(request, 'login_register/home.html')

def registrationform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        country = request.POST.get('country')
        hobbies = request.POST.getlist('hobbies')
        mobile_number = request.POST.get('mobile_number')
        profile_picture = request.FILES['profile_picture']
        try:
            user = User.objects.create_user(username=username, first_name=first_name, 
                                            last_name=last_name, email=email, password=password)
            userprofile = UserProfile.objects.create(user=user, gender=gender, birth_date=birth_date, 
                                                    country=country, profile_picture=profile_picture, 
                                                    hobbies=hobbies, mobile_number=mobile_number)
            deactivate_user(user.id)
            activateEmail(request, user, email)
            userprofile.save()
            return redirect('home')
        except Exception as e:
            return HttpResponse(f"Error creating user: {e}", status=500)
    context = {
            'countries': countries,
            'hobbies': UserProfile.HOBBIES_CHOICES,
            'gender': UserProfile.GENDER_CHOICES,
            }
    return render(request, 'login_register/registrationform.html', context)

def activateEmail(request, user, to_email):
    """_summary_

    Args:
        request (_type_): _description_
        user (_type_): _description_
        to_email (_type_): _description_
    """
    mail_subject = 'Activate your user account.'
    message = render_to_string('login_register/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

def activate(request, uidb64, token):
    """_summary_

    Args:
        request (_type_): _description_
        uidb64 (_type_): _description_
        token (_type_): _description_

    Returns:
        _type_: _description_
    """
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        if user.is_active:
            messages.info(request, 'Account already activated.')
            return redirect('loginform')
        else:
            user.is_active = True
            user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('loginform')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('home')

def loginform(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('loginform')
    return render(request, 'login_register/login_form.html')

def resetpassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            password_pattern = r"/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/"
            user = request.user
            if user.check_password(old_password):
                if old_password != new_password:
                    if new_password == confirm_password:
                        if not re.match(password_pattern, new_password):
                            messages.error(request, 'Password must contain at least 8 characters, one uppercase letter, one lowercase letter, one number and one special character.')
                            return redirect('resetpassword')
                        else:
                            user.set_password(new_password)
                            user.save()
                            messages.success(request, 'Password changed successfully.')
                            return redirect('loginform')
                    else:
                        messages.error(request, 'New password and confirm password do not match.')
                        return redirect('resetpassword')
                else:
                    messages.error(request, 'New password cannot be the same as old password.')
                    return redirect('resetpassword')
            else:
                messages.error(request, 'Old password is incorrect.')
                return redirect('resetpassword')
        else:
            return render(request, 'login_register/resetpassword.html')
    else:
        messages.error(request, 'You must be logged in to reset your password.')
        return redirect('loginform')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        age = UserProfile.get_age(userprofile)
        context = {
            'user': user,
            'userprofile': userprofile,
            'age': age,
        }
        return render(request, 'login_register/profile.html', context)
    else:
        return redirect('loginform')

def user_logout(request):
    logout(request)
    return render(request, 'login_register/home.html')