"""myFirstDjangoProject URL Configuration

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
from django.urls import path
from myFirstDjangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage), #homepage
    path('about-us/', views.aboutUs), #connecting urls and views
    path('courses/', views.Course),
    path('contact/', views.contact),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd),
    path('courses/<int:courseid>', views.courseDetails), #we can use <str: var_name> or <slug: var_name> as well
    # if you are not clear with the data type then simply pass the data e.g. courses/<courseid>

]
