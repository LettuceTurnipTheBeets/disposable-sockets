from django import forms

class RoomForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=20, strip=True, label='Username')
    room_name = forms.CharField(min_length=1, max_length=50, strip=True, required=False, label='Room Name')

class CodeForm(forms.Form):
    code = forms.CharField(min_length=4, max_length=4, required=True, label='Room Code')
