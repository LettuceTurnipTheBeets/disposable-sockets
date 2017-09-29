from django import forms
from sockets.models.rooms import Room
from django.core.exceptions import ObjectDoesNotExist

class RoomForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=20, strip=True, label='Username')
    room_name = forms.CharField(min_length=1, max_length=50, strip=True, required=False, label='Room Name')

class CodeForm(forms.Form):
    code = forms.CharField(min_length=4, max_length=4, required=True, label='Room Code')

class NameForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=20, required=True, label='Name')

class ChatForm(forms.Form):
    message = forms.CharField(min_length=1, max_length=144, required=True, label='Chat')

    def clean(self):
        message = self.cleaned_data.get('message', None)
        if message:
            message = message.strip()

        return self.cleaned_data
