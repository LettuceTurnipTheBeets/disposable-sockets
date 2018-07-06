from django.test import TestCase
from sockets.forms import RoomForm, CodeForm, NameForm, ChatForm


class FormTest(TestCase):
    
    def test_room_form_labels(self):
        form = RoomForm()
        self.assertTrue(form.fields['username'].label == 'Username' and form.fields['room_name'].label == 'Room Name')

    def test_room_form_min_max(self):
        form_data1 = {'username': 'Greg', 'room_name': 'Party Room'}
        form_data2 = {'username': 'Charlie', 'room_name': ''}
        form_data3 = {'username': 'This Username Is Much Too Long', 'room_name': 'Party Palace'}
        form_data4 = {'username': 'Jill', 'room_name': 'We start by importing our form and some Python and Django libraries to help test time-related functionality. We then declare our form test class in the same way as we did for models, using a descriptive name for our TestCase-derived test class.'}
        form_data5 = {'username': '', 'room_name': 'Party Room'}

        form1 = RoomForm(data=form_data1)
        form2 = RoomForm(data=form_data2)
        form3 = RoomForm(data=form_data3)
        form4 = RoomForm(data=form_data4)
        form5 = RoomForm(data=form_data5)
        
        self.assertTrue(form1.is_valid())
        self.assertTrue(form2.is_valid())
        self.assertFalse(form3.is_valid())
        self.assertFalse(form4.is_valid())
        self.assertFalse(form5.is_valid())

    def test_code_form_labels(self):
        form = CodeForm()
        self.assertTrue(form.fields['code'].label == 'Room Code')

    def test_code_form_min_max(self):
        form_data1 = {'code': 'abcd'}
        form_data2 = {'code': 'Y'}
        form_data3 = {'code': 'abcdefg'}

        form1 = CodeForm(data=form_data1)
        form2 = CodeForm(data=form_data2)
        form3 = CodeForm(data=form_data3)

        self.assertTrue(form1.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertFalse(form3.is_valid())

    def test_name_form_labels(self):
        form = NameForm()
        self.assertTrue(form.fields['name'].label == 'Name')

    def test_name_form_min_max(self):
        form_data1 = {'name': 'Jeremy'}
        form_data2 = {'name': ''}
        form_data3 = {'name': 'This Name Is Much Too Long'}

        form1 = NameForm(data=form_data1)
        form2 = NameForm(data=form_data2)
        form3 = NameForm(data=form_data3)

        self.assertTrue(form1.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertFalse(form3.is_valid())

    def test_chat_form_labels(self):
        form = ChatForm()
        self.assertTrue(form.fields['message'].label == 'Chat')

    def test_chat_form_min_max(self):
        form_data1 = {'message': 'Hello'}
        form_data2 = {'name': ''}
        form_data3 = {'name': 'Code coverage describes how much source code has been tested. It shows which parts of your code are being exercised by tests and which are not. It’s an important part of testing applications, so it’s strongly recommended to check the coverage of your tests.'}

        form1 = ChatForm(data=form_data1)
        form2 = ChatForm(data=form_data2)
        form3 = ChatForm(data=form_data3)

        self.assertTrue(form1.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertFalse(form3.is_valid())
