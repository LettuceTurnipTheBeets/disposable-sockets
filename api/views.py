from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from .forms import RoomForm, CodeForm, NameForm
from api.models.rooms import Room
from datetime import datetime, timedelta


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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            room_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            url_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            room_length = 4
            url_length = 10
            room_code = ""
            url = ""

            for i in range(room_length):
                next_index = random.randrange(len(room_alphabet))
                room_code = room_code + room_alphabet[next_index]

            for i in range(url_length):
                next_index = random.randrange(len(url_alphabet))
                url = url + url_alphabet[next_index]
            
            obj = Room.objects.create(
                admin=room_form.cleaned_data['username'],
                name=room_form.cleaned_data['room_name'],
                code=room_code,
                url=url,
            )

            print (room_code)
            print (url)
            return redirect('/{}/'.format(obj.url))

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
                room = Room.objects.all().filter(code=code_form.cleaned_data['code'])[0]
            except:
                raise Http404
                # reload index
            
            if room.code in request.COOKIES:            
                return redirect('/{}/'.format(room.url))
            else:
                #return redirect('/registration/?room={}'.format(room.code))
                return render(request, 'registration.html', {'form': NameForm(), 'room_code': room.code})
    else:
        code_form  = CodeForm()

    return render(request, 'index.html', {'code_form': code_form, 'room_form': room_form})

"""
Registration Page
"""
def registration(request):
    #room_code = request.GET.get('room')
    
    if request.method == 'POST':
        form = NameForm(request.POST)
        room_code  = request.POST.get('room_code')
        print(room_code)

        if form.is_valid():
            room = Room.objects.all().filter(code=room_code)[0]

            response = redirect('/{}/'.format(room.url))
            response.set_cookie(room.code, form.cleaned_data['name'], max_age=300)
            
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
def room(request, room_url):
    try:
        room = Room.objects.all().filter(url=room_url)[0]
    except IndexError:
        raise Http404

    if room.code in request.COOKIES:
        name = request.COOKIES.get(room.code)

    return render(request, 'room.html', {'room': room, 'name': name})    

