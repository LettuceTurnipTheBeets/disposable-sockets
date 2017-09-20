from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from .forms import RoomForm, CodeForm, NameForm, ChatForm
from sockets.models.rooms import Room
from sockets.models.chat import Chat
from sockets.models.guests import Guest
from datetime import datetime, timedelta
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import re, io
from base64 import decodestring
from django.core.files import File


def index(request):
    """
    Index/Home/Landing Page
    """
    code_form = CodeForm()
    try:
        total = Room.objects.first().id
    except AttributeError:
        total = 0

    total_hours = Room.objects.count() * 24 
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
                        created=timezone.now().replace(microsecond=0),
                    )
                    room_condition = False
                except IntegrityError:
                    pass

            print ('Create room '.format(room_code))
            obj.guests.create(
                user=obj.admin,
            )            
            request.session[obj.code] = obj.admin
            request.session.set_expiry(3600)
            # max_age=86400 for a day 
     
            return redirect('/{}'.format(obj.code))

    # if a GET (or any other method) we'll create a blank form
    else:
        room_form = RoomForm()

    return render(
        request,
        'index.html', {
            'room_form': room_form,
            'code_form': code_form,
            'total': total,
            'total_hours': total_hours,
        }
    )

def join(request):
    """
    Join Endpoint
    """
    room_form = RoomForm()

    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        
        if code_form.is_valid():
            try:
                room = Room.objects.get(code=code_form.cleaned_data['code'])
            except:
                raise Http404
            
            if room.code in request.session:          
                return redirect('/{}/'.format(room.code))
            else:
                return render(
                    request,
                    'registration.html',
                    {'form': NameForm(), 'room_code': room.code}
                )
    else:
        code_form  = CodeForm()

    return render(
        request,
        'index.html', {
            'code_form': code_form,
            'room_form': room_form,
        },
    )

def registration(request):
    """
    Registration Page
    """  
    if request.method == 'POST':
        form = NameForm(request.POST)
        room_code = request.POST.get('room_code')
        print(room_code)

        if form.is_valid():
            room = Room.objects.get(code=room_code)
            name = form.cleaned_data['name']       
            message = '{} is already in use.  Please enter a new name.'            

            try:
                room.guests.get(user=name)

                return render(
                    request,
                    'registration.html', {
                    'form': form,
                    'error_message': message.format(form.cleaned_data['name']),
                    'room_code': room_code,
                    }
                )
            except ObjectDoesNotExist:
                obj = room.guests.create(
                    user=name,
                )
             
            request.session[room.code] = form.cleaned_data['name']
            request.session.set_expiry(3600)
            # max_age depends on when the room expires
            # use the below code if/when a room lasts 1 day
            # max_age =  (room.expires() - timezone.now()).seconds + 900
            # the 900 is the script frequency 900 seconds = 15 minutes
             
            return redirect('/{}/'.format(room.code))

        else:
            return redirect('/registration/')

    else:
        form = NameForm() 
  
    return render(
        request,
        'registration.html', {
            'form': form,
            'error_message': '',
        }
    )  

def about(request):
    """
    About Page
    """
    return render(
        request,
        'about.html'
    )

def room(request, code):
    """
    Room Detail Page
    """
    try:
        room = Room.objects.get(code=code)
    except IndexError:
        raise Http404

    guests = room.guests.all()
    
    if room.code in request.session:
        name = request.session[room.code]
    else:
        raise Http404

    return render(
        request,
        'room.html', {
            'room': room, 
            'guests': guests,
            'name': name,
            'chat_form': ChatForm(),
        }
    )    
