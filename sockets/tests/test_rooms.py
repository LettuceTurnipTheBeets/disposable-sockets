from django.test import TestCase
from django.utils import timezone
from sockets.models.rooms import Room


class RoomTestCase(TestCase):
    """Test the disposable chat rooms"""
    def setUp(self):
        Room.objects.create(
            admin="Test Admin 1",
            code="dkgh",
            created=timezone.now().replace(microsecond=0),
        )
        Room.objects.create(
            admin="Test Admin 2",
            code="abcd",
            created=timezone.now().replace(microsecond=0),
        )
        Room.objects.create(
            admin="Test Admin 3",
            code="gkit",
            created=timezone.now().replace(microsecond=0),
        )

    def test_code(self):
        self.assertEqual(Room.objects.get(code="dkgh").code, "dkgh")
        self.assertEqual(Room.objects.get(code="abcd").code, "abcd")
        self.assertEqual(Room.objects.get(code="gkit").code, "gkit")

    def test_admin(self):
        self.assertEqual(Room.objects.get(code="dkgh").admin, "Test Admin 1") 
        self.assertEqual(Room.objects.get(code="abcd").admin, "Test Admin 2")
        self.assertEqual(Room.objects.get(code="gkit").admin, "Test Admin 3")

    def test_created(self):
        self.assertGreater(timezone.now(), Room.objects.get(code="dkgh").created)
        self.assertGreater(timezone.now(), Room.objects.get(code="abcd").created)
        self.assertGreater(timezone.now(), Room.objects.get(code="gkit").created)

    def test_description(self):
        self.assertEqual(Room.objects.get(code="dkgh").description, '')
        self.assertEqual(Room.objects.get(code="abcd").description, '')
        self.assertEqual(Room.objects.get(code="gkit").description, '')
