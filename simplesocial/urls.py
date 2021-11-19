"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('',views.Homepage.as_view(),name='home'),
    path('feedbacks/',views.Feedbacks.as_view(),name='feedback'),
    path('UserAccounts/',include('UserAccounts.urls',namespace='UserAccounts')),
    path('UserAccounts/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('admin/', admin.site.urls),
    path('posts/',include('posts.urls',namespace='posts')),
    path('groups/',include('groups.urls',namespace='groups')),
    path('loc_criminal/',include('loc_criminal.urls', namespace = 'loc_criminal'))
]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
