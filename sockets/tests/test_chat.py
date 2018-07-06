from django.test import TestCase
from django.utils import timezone
from sockets.models.rooms import Room
from sockets.models.guests import Guest
from sockets.models.chat import Chat


class ChatTestCase(TestCase):
    """Test the real-time chat"""
    def setUp(self):
        room1 = Room.objects.create(
            admin="Test Chat 1",
            code="aJJh",
            created=timezone.now().replace(microsecond=0),
        )
        room2 = Room.objects.create(
            admin="Test Chat 2",
            code="abcd",
            created=timezone.now().replace(microsecond=0),
        )
        room3 = Room.objects.create(
            admin="Test Chat 3",
            code="gkit",
            created=timezone.now().replace(microsecond=0),
        )

        room1.guests.create(
            user = 'Jake',
        )
        room2.guests.create(
            user = 'John',
        )
        room3.guests.create(
            user = 'Jane',
        )

        room1.chat.create(
            name='Jake',
            message='Hello',
            time=timezone.now().replace(microsecond=0),
        )
        room1.chat.create(
            name='Test Chat 1',
            message='Hi',
            time=timezone.now().replace(microsecond=0),
        )
        room2.chat.create(
            name='John',
            message='Hello',
            time=timezone.now().replace(microsecond=0),
        )
        room2.chat.create(
            name='Test Chat 2',
            message='Hi',
            time=timezone.now().replace(microsecond=0),
        )
        room3.chat.create(
            name='Jane',
            message='Hello',
            time=timezone.now().replace(microsecond=0),
        )
        room3.chat.create(
            name='Test Chat 3',
            message='Hi',
            time=timezone.now().replace(microsecond=0),
        )

    def test_name(self):
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(message='Hello').name, 'Jake')
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(message='Hi').name, 'Test Chat 1')
        self.assertEqual(Room.objects.get(code="abcd").chat.get(message='Hello').name, 'John')
        self.assertEqual(Room.objects.get(code="abcd").chat.get(message='Hi').name, 'Test Chat 2')
        self.assertEqual(Room.objects.get(code="gkit").chat.get(message='Hello').name, 'Jane')
        self.assertEqual(Room.objects.get(code="gkit").chat.get(message='Hi').name, 'Test Chat 3')

    def test_message(self):
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(name='Jake').message, 'Hello')
        self.assertEqual(Room.objects.get(code="aJJh").chat.get(name='Test Chat 1').message, 'Hi')
        self.assertEqual(Room.objects.get(code="abcd").chat.get(name='John').message, 'Hello')
        self.assertEqual(Room.objects.get(code="abcd").chat.get(name='Test Chat 2').message, 'Hi')
        self.assertEqual(Room.objects.get(code="gkit").chat.get(name='Jane').message, 'Hello')
        self.assertEqual(Room.objects.get(code="gkit").chat.get(name='Test Chat 3').message, 'Hi')

    def test_time(self):
        self.assertGreater(timezone.now(), Room.objects.get(code="aJJh").chat.get(name='Jake').time)
        self.assertGreater(timezone.now(), Room.objects.get(code="aJJh").chat.get(name='Test Chat 1').time)
        self.assertGreater(timezone.now(), Room.objects.get(code="abcd").chat.get(name='John').time)
        self.assertGreater(timezone.now(), Room.objects.get(code="abcd").chat.get(name='Test Chat 2').time)
        self.assertGreater(timezone.now(), Room.objects.get(code="gkit").chat.get(name='Jane').time)
        self.assertGreater(timezone.now(), Room.objects.get(code="gkit").chat.get(name='Test Chat 3').time)

    def test_chat(self):
        self.assertEqual(Chat.objects.all()[0].name, 'Jake')
        self.assertEqual(Chat.objects.all()[1].name, 'Test Chat 1')
        self.assertEqual(Chat.objects.all()[2].name, 'John')
        self.assertEqual(Chat.objects.all()[3].name, 'Test Chat 2')
        self.assertEqual(Chat.objects.all()[4].name, 'Jane')
        self.assertEqual(Chat.objects.all()[5].name, 'Test Chat 3')
        self.assertEqual(Chat.objects.count(), 6)

