"""Webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from auto import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    
    path('admin/', admin.site.urls),
    re_path(r'^$', views.loginn),
    path('index/',views.index),
    path('register/', views.register),
    path('about/', views.about),
    path('contact/', views.contact),
    path('Search/',views.Search),
    path('checklog/',views.check_user),
    path('logout/',views.ulogout),
    path('login/',views.loginn),
    path('allcar/',views.dropdown.d_all),
    path('coupe/',views.dropdown.d_Coupe),
    path('hback/',views.dropdown.d_Hatchback),
    path('sedan/',views.dropdown.d_Sedan),
    path('suv/',views.dropdown.d_SUV),
    path('sports/',views.dropdown.d_Sports),
    path('supercar/',views.dropdown.d_Supercar),
    path('van/',views.dropdown.d_Van),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

