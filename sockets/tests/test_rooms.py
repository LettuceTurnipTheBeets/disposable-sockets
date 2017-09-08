from django.test import TestCase
from sockets.models.rooms import Room
from django.utils import timezone


class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(
            admin="Test Admin 1",
            code="dkgh",
            created=timezone.now().replace(microsecond=0),
        )

    def test_code(self):
        self.assertEqual(Room.objects.get(code="dkgh").code, "dkgh")

    def test_admin(self):
        self.assertEqual(Room.objects.get(code="dkgh").admin, "Test Admin 1") 

    def test_created(self):
        self.assertGreater(timezone.now(), Room.objects.get(code="dkgh").created)

    def test_description(self):
        self.assertEqual(Room.objects.get(code="dkgh").description, '')
