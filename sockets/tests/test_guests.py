from django.test import TestCase
from django.utils import timezone
from sockets.models.rooms import Room
from sockets.models.guests import Guest


class GuestTestCase(TestCase):
    """Test the guests that are registered to a room"""
    def setUp(self):
        room1 = Room.objects.create(
            admin="Test Guests 1",
            code="vWkd",
            created=timezone.now().replace(microsecond=0),
        )
        room2 = Room.objects.create(
            admin="Test Guests 2",
            code="abcd",
            created=timezone.now().replace(microsecond=0),
        )
        room3 = Room.objects.create(
            admin="Test Guests 3",
            code="gkit",
            created=timezone.now().replace(microsecond=0),
        )

        room1.guests.create(
            user = 'Jake',
        )
        room1.guests.create(
            user = 'Layne',
        )
        room2.guests.create(
            user = 'John',
        )
        room2.guests.create(
            user = 'Luke',
        )
        room3.guests.create(
            user = 'Jane',
        )
        room3.guests.create(
            user = 'Lonny',
        )

    def test_guest(self):
        self.assertEqual(Room.objects.get(code="vWkd").guests.get(user="Jake").user, 'Jake')
        self.assertEqual(Room.objects.get(code="vWkd").guests.get(user="Layne").user, 'Layne')
        self.assertEqual(Room.objects.get(code="vWkd").guests.count(), 2)
        self.assertEqual(Room.objects.get(code="abcd").guests.get(user="John").user, 'John')
        self.assertEqual(Room.objects.get(code="abcd").guests.get(user="Luke").user, 'Luke')
        self.assertEqual(Room.objects.get(code="abcd").guests.count(), 2)
        self.assertEqual(Room.objects.get(code="gkit").guests.get(user="Jane").user, 'Jane')
        self.assertEqual(Room.objects.get(code="gkit").guests.get(user="Lonny").user, 'Lonny')
        self.assertEqual(Room.objects.get(code="gkit").guests.count(), 2)

    def test_room(self):
        self.assertEqual(Guest.objects.all()[0].user, 'Jake')
        self.assertEqual(Guest.objects.all()[1].user, 'Layne')
        self.assertEqual(Guest.objects.all()[2].user, 'John')
        self.assertEqual(Guest.objects.all()[3].user, 'Luke')
        self.assertEqual(Guest.objects.all()[4].user, 'Jane')
        self.assertEqual(Guest.objects.all()[5].user, 'Lonny')
        self.assertEqual(Guest.objects.count(), 6)
