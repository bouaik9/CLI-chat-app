from django.test import TestCase
from .models import Room, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class RoomModelTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name='Test Room', slug='test-room')

    def test_room_creation(self):
        self.assertEqual(self.room.name, 'Test Room')
        self.assertEqual(self.room.slug, 'test-room')

class MessageModelTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name='Test Room', slug='test-room')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.message = Message.objects.create(room=self.room, user=self.user, content='Hello, world!')

    def test_message_creation(self):
        self.assertEqual(self.message.content, 'Hello, world!')
        self.assertEqual(self.message.room, self.room)
        self.assertEqual(self.message.user, self.user)
        self.assertFalse(self.message.is_flagged)