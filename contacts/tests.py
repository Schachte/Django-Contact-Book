from django.test import TestCase

from contacts.models import Contact 

# Create your tests here.
class ContactsTest(TestCase):
	def test_str(self):
		c = Contact(first_name="Ryan", last_name="Schachte")
		self.assertEqual(str(c), 'Ryan Schachte')