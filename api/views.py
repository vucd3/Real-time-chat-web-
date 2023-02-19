from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import datetime

# Create your views here.
def main(request):
    return render(request, 'login.html') 

def save_user(request):
    user_name = request.POST.get('username')

    if not User.objects.filter(name = user_name).exists():
        new_user = User.objects.create(name = user_name)
        new_user.save()
    return redirect('/'+user_name)

def chat_box(request, user):
    rooms = Room.objects.all()
    lst_room = [room['room'] for room in list(rooms.values())]

    return render(request, 'chat_box.html', {'rooms': lst_room, 'user': user})

def create_room(request):
    user = request.POST.get('user')
    room = request.POST.get('room_name')
    if not Room.objects.filter(room=room).exists():
        new_room = Room.objects.create(room=room)
        new_room.save()

    room = Room.objects.get(room=room)
    return render(request, 'room.html', {"room": room, "user": user})

def send_message(request):
    msg = request.POST.get("message")
    room_name = request.POST.get("room_id")
    user_name = request.POST.get("username")
    current_time = datetime.datetime.now()
    new_message = Message.objects.create(value=msg, datetime = current_time, room=room_name, user=user_name)
    new_message.save()
    return JsonResponse({"Message": "Send message succesfully!"})

def get_messages(request, room):
    room_details = Room.objects.get(room=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def room_detail(request, room, user):
    room_details = Room.objects.get(room=room)
    messages = Message.objects.filter(room=room_details.id)
    return render(request, 'room.html', {"user": user, "room": room_details, "messages":list(messages.values())})
