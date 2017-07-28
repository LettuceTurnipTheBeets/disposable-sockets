from django import forms
from api.models.rooms import Room

class RoomForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=20, strip=True, label='Username')
    room_name = forms.CharField(min_length=1, max_length=50, strip=True, required=False, label='Room Name')

class CodeForm(forms.Form):
    code = forms.CharField(min_length=4, max_length=4, required=True, label='Room Code')

    def clean(self):
        cd = self.cleaned_data

        if len(Room.objects.all().filter(code=self.cleaned_data['code'])) == 0:
            self.add_error('code', 'No room exists with that code.')
        return cd

class NameForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=20, required=True, label='Name')
