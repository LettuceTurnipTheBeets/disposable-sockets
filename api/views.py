from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from .forms import RoomForm, CodeForm, NameForm, ChatForm
from api.models.rooms import Room
from api.models.chat import Chat
from api.models.guests import Guest
from datetime import datetime, timedelta
from django.db import IntegrityError
from django.utils import timezone


"""
Index/Home/Landing Page
"""
def index(request):
    code_form = CodeForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        room_form = RoomForm(request.POST)
        # check whether it's valid:
        if room_form.is_valid():
            room_condition = True 
            room_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            room_length = 4

            while room_condition:
                room_code = ""
                
                for i in range(room_length):
                    next_index = random.randrange(len(room_alphabet))
                    room_code = room_code + room_alphabet[next_index]

                """
                Check that the room code is unique.
                I'm querying the database every time because it may change before a 
                successful code is generated.
                """
                                        
                try:
                    obj = Room.objects.create(
                        admin=room_form.cleaned_data['username'],
                        name=room_form.cleaned_data['room_name'],
                        code=room_code,
                    )
                    room_condition = False
                except IntegrityError:
                    pass

            print (room_code)

            response = redirect('/{}'.format(obj.code))
            response.set_cookie(obj.code, obj.admin, max_age=300)
            # max_age=86400 for a day 
     
            return response

    # if a GET (or any other method) we'll create a blank form
    else:
        room_form = RoomForm()

    return render(request, 'index.html', {'room_form': room_form, 'code_form': code_form})

"""
Join Endpoint
"""
def join(request):
    room_form = RoomForm()

    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        
        if code_form.is_valid():
            try:
                room = Room.objects.get(code=code_form.cleaned_data['code'])
            except:
                raise Http404
            
            if room.code in request.COOKIES:            
                return redirect('/{}/'.format(room.code))
            else:
                return render(request, 'registration.html', {'form': NameForm(), 'room_code': room.code})
    else:
        code_form  = CodeForm()

    return render(request, 'index.html', {'code_form': code_form, 'room_form': room_form})

"""
Registration Page
"""
def registration(request):  
    if request.method == 'POST':
        form = NameForm(request.POST)
        room_code  = request.POST.get('room_code')
        print(room_code)

        if form.is_valid():
            room = Room.objects.get(code=room_code)

            room.guests.create(
                user=form.cleaned_data['name'],
            )
            response = redirect('/{}/'.format(room.code))
            response.set_cookie(room.code, form.cleaned_data['name'], max_age=300)
            # max_age depends on when the room expires
            # use the below code if/when a room lasts 1 day
            # max_age =  (room.expires() - timezone.now()).seconds + 900
            # the 900 is the script frequency 900 seconds = 15 minutes
             
            return response

        else:
            return redirect('/registration/')

    else:
        form = NameForm() 
  
    return render(request, 'registration.html', {'form': form})  

"""
About Page
"""
def about(request):
     return render(request, 'about.html')

"""
Room Detail Page
"""
def room(request, code):
    try:
        room = Room.objects.get(code=code)
    except IndexError:
        raise Http404

    guests = room.guests.all()
    
    if room.code in request.COOKIES:
        name = request.COOKIES.get(room.code)
    else:
        raise Http404

    return render(request, 'room.html', {'room': room, 'guests': guests, 'name': name, 'chat_form': ChatForm()})

"""
Chat
"""
def chat(request, code):   
    print(code)
    if request.method == 'POST':
        chat_form = ChatForm(request.POST)
        room = Room.objects.get(code=code)

        if chat_form.is_valid():
            name = request.COOKIES.get(room.code)

            room.chat.create(
                message=chat_form.cleaned_data['message'],
                name=name,
            )

        return redirect('/{}/'.format(room.code))
    else:
        raise Http404        
