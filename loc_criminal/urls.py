from loc_criminal import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='loc_criminal'

urlpatterns=[
    path('',views.CriminalListView.as_view(),name='criminal'),
]
