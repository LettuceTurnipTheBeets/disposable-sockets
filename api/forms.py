from django import forms

class RoomForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=20, strip=True, label='Username')
    room_name = forms.CharField(min_length=1, max_length=50, strip=True, required=False, label='Room Name')
