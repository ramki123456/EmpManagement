"""Sudheer_Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from MyApp import views
from Task import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^load/', views.WelcomeView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^home/', views.HomePageView.as_view()),
    url(r'^logout/', views.LogoutView.as_view()),
    url(r'^update/(?P<emp_num>[-\d]+)', views.UpdateView.as_view()),
    url(r'^update_data/', views.UpdateDataView.as_view()),
    # url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^delete/(?P<emp_num>[-\d]+)', views.DeleteView.as_view()),
    url(r'^addemp/', views.AddEmployee.as_view()),
    url(r'^add_emp_data/', views.AddEmpView.as_view()),
    
]
