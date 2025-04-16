"""
URL configuration for signup_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login_register import views
from django.conf.urls.static import static
from django.conf import settings
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('register/', views.registrationform, name='registrationform'),
    path('login/', views.loginform, name='loginform'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('email/', include(email_urls), name='email-verification'),	
    path('reset/', views.resetpassword, name='resetpassword'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
