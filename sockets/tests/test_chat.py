from django.test import TestCase
from django.utils import timezone
from sockets.models.rooms import Room
from sockets.models.guests import Guest
from sockets.models.chat import Chat


class ChatTestCase(TestCase):
    """Test the real-time chat"""
    def setUp(self):
        room = Room.objects.create(
            admin="Test Chat 1",
            code="aJJh",
            created=timezone.now().replace(microsecond=0),
        )

        room.guests.create(
            user = 'Jake',
        )

        room.chat.create(
            name='Jake',
            message='Hello',
            time=timezone.now().replace(microsecond=0),
        )

        room.chat.create(
            name='Test Chat 1',
            message='Hi',
            time=timezone.now().replace(microsecond=0),
        )

    def test_name(self):
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(message='Hello').name, 'Jake')
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(message='Hi').name, 'Test Chat 1')

    def test_message(self):
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(name='Jake').message, 'Hello')
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(name='Test Chat 1').message, 'Hi')

    def test_time(self):
        self.assertGreater(timezone.now(), Room.objects.get(code="aJJh").chat.get(name='Jake').time)
        self.assertGreater(timezone.now(), Room.objects.get(code="aJJh").chat.get(name='Test Chat 1').time)

    def test_chat(self):
        self.assertEqual(Chat.objects.all()[0].name, 'Jake')
        self.assertEqual(Chat.objects.all()[1].name, 'Test Chat 1')
        self.assertEqual(Chat.objects.count(), 2)

