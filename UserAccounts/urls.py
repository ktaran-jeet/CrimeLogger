from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='UserAccounts'

urlpatterns = [
path('login/',views.user_login,name='login'),
path('logout/',auth_views.LogoutView.as_view(),name='logout'),
path('signup/',views.signup,name='signup'),
path('otp_request/',views.otp_request,name='otp_request'),
]
