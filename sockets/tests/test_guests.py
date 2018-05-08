from django.test import TestCase
from django.utils import timezone
from sockets.models.rooms import Room
from sockets.models.guests import Guest


class GuestTestCase(TestCase):
    """Test the guests that are registered to a room"""
    def setUp(self):
        room = Room.objects.create(
            admin="Test Guests 1",
            code="vWkd",
            created=timezone.now().replace(microsecond=0),
        )

        room.guests.create(
            user = 'Jake',
        )

        room.guests.create(
            user = 'Layne',
        )

    def test_guest(self):
        self.assertEqual(Room.objects.get(code="vWkd").guests.get(user="Jake").user, 'Jake')
        self.assertEqual(Room.objects.get(code="vWkd").guests.get(user="Layne").user, 'Layne')
        self.assertEqual(Room.objects.get(code="vWkd").guests.count(), 2)

    def test_room(self):
        self.assertEqual(Guest.objects.count(), 2)
        self.assertEqual(Guest.objects.all()[0].user, 'Jake')
        self.assertEqual(Guest.objects.all()[1].user, 'Layne')
