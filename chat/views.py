from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages # Import messages for user feedback             
from .tasks import moderate_message
from django.http import HttpResponse
from django.http import JsonResponse

def room_detail(request, slug):
    if not request.user.is_authenticated:
        print('yes')
        return redirect('login')
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room).order_by('-timestamp')
    return render(request, 'chat/room_detail.html', {'room': room, 'messages': messages})

def room_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    rooms = Room.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})


def send_message(request):
    if request.method == 'POST':
        room_slug = request.POST.get('room_slug')
        content = request.POST.get('content')
        room = Room.objects.get(slug=room_slug)
        user = User.objects.get(username=request.user.username)  # Assuming user is authenticated
        message = Message.objects.create(user=user, room=room, content=content)
        # Here you would typically call a Celery task to send the message
        moderate_message.delay(message.id)  # Call the moderation task asynchronously
        # send_message_task.delay(message.id)
        
        return render(request, 'chat/room_detail.html', {'room': room, 'messages': [message]})
    return render(request, 'chat/send_message.html')


def fetch_messages(request, slug):
    try:
        room = Room.objects.get(slug=slug)
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    messages_data = [
        {
            'id': msg.id,
            'user': msg.user.username,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime('%H:%S'),
            'is_flagged': msg.is_flagged,
        }
        for msg in messages
    ]
    return JsonResponse({'messages': messages_data})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('good')
            return redirect('room_list')
        
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chat/login.html')