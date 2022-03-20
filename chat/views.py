from django.shortcuts import render,redirect
from .models import Room,Messages
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


def room(request,room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    
    return render(request,'room.html',{
        'username':username,
        'room':room,
        'room_details':room_details
    })

def checkview(request):
    roomname = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=roomname).exists():
        return redirect("/" + roomname + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=roomname)
        new_room.save()
        return redirect("/" + roomname + "/?username=" + username)

def send(request):
    user = request.POST['username']
    id_room = request.POST['room_id']
    text = request.POST['message']
    
    new_message = Messages.objects.create(value=text,user=user,room=id_room)
    new_message.save()
    
    return HttpResponse("message sent succesfully")

def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    
    messages = Messages.objects.filter(room=room_details.id)
    
    return JsonResponse({"messages":list(messages.values())})