"""my_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from profiles.views import (
    login_view,
    logout_view,
    register_view,
    edit_user,
    detail_user,
    list_users,
    )
from list_trans.views import (
    index,
    all_car, 
    detail_car, 
    delete_car,
    create_car,
    edit_car
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/', logout_view),
    path('login/',login_view),
    path('register/', register_view),
    path('allcar/', all_car, name='all_car'),
    path('allcar/car/<int:pk>/', detail_car, name='detail_car'),
    path('car/create/', create_car, name='create_car'),
    path('allcar/car/delete/<int:pk>/', delete_car),
    path('allcar/car/edit/<int:pk>/', edit_car),
    path('profile/<int:pk>/', detail_user),
    path('profile/edit/<int:pk>/', edit_user),
    path('list_users/', list_users),
]
