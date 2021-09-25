import unittest
from classes import Message

class TestMessageInit(unittest.TestCase):
    
    # test that the attributes get assigned correctly
    def test_attr(self):
        message = Message("this is a test message")
        self.assertEqual(message.text, "<this is a test message>")
    
    # test that the message doesn't get important data stripped out of it
    def test_begins_with_b(self):
        message = Message("bthis is a test message")
        self.assertEqual(message.text, "<bthis is a test message>")

    def test_buffer_overflow(self):
        message=Message(9999*"hello")
        self.assertLess(len(bytes(message.text, "utf-8")), 1025)