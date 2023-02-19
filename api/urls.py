"""chatting_web URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:user>/', views.chat_box, name='chat_box'),
    path('saveuser', views.save_user, name ='saveuser'),
    path('create_room', views.create_room, name='create_room'),
    path('send', views.send_message, name='send'),
    path('getMessages/<str:room>', views.get_messages, name = 'getMessages'),
    path('rooms/<str:room>/<str:user>', views.room_detail, name = 'room_detail')
]
