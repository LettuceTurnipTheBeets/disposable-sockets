from django.test import TestCase
from sockets.models.rooms import Room

class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(
            admin="Test Admin 1",
            code="dkgh",
        )

    def test_code(self):
        self.assertEqual(Room.objects.get(code="dkgh").code, "dkgh")
