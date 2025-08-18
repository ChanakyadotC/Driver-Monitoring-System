"""FatigueDetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from DriverDrowsiness import views as mainView
from users import views as usr
from admins import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel

    # Main Application Routes
    path('', mainView.index, name='index'),  # Home page
    path('logout/', mainView.logout, name='logout'),  # Logout
    path('autoist-login/', mainView.AutoistLogin, name='AutoistLogin'),  # Autoist Login
    path('admin-login/', mainView.AdminLogin, name='AdminLogin'),  # Admin Login
    path('autoist-register/', mainView.AutoistRegister, name='AutoistRegister'),  # Autoist Registration

    # User Side Routes
    path('driver-register-actions/', usr.DriverRegisterActions, name='DriverRegisterActions'),  # Driver Registration Actions
    path('autoist-login-check/', usr.AutoistLoginCheck, name='AutoistLoginCheck'),  # Autoist Login Check
    path('autoist-home/', usr.AutoistHome, name='AutoistHome'),  # Autoist Home
    path('detect-fatigue-driver/', usr.DetectFatigueDriver, name='DetectFatigueDriver'),  # Detect Fatigue
    path('start-training/', usr.StartTraining, name='StartTraining'),  # Start Training
    path('autoist-history/', usr.Autoisthistory, name='Autoisthistory'),  # Autoist History

    # Admin Side Routes
    path('admin/login-check/', admins.AdminLoginCheck, name='AdminLoginCheck'),  # Admin Login Check
    path('admin/home/', admins.AdminHome, name='AdminHome'),  # Admin Home
    path('admin/view-registered-autoists/', admins.ViewRegisteredAutoists, name='ViewRegisteredAutoists'),  # View Registered Autoists
    path('admin/activate-autoists/', admins.AdminActivaAutoists, name='AdminActivaAutoists'),  # Activate Autoists
    path('admin/delete-autoists/', admins.AdminDeleteAutoists, name='AdminDeleteAutoists'),  # Delete Autoists
    path('admin/view-fatigue-history/', admins.AdminViewFatigueHistory, name='AdminViewFatigueHistory'),  # View Fatigue History
]
