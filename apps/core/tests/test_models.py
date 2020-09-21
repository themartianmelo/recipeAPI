from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # Tests whether the user creation with email is successful
        email    = "nebumathomkuttan@gmail.com"
        password = "daddyamma"
        user     = get_user_model().objects.create_user(
                        email    = email,
                        password = password    
                   )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email    = "nebumathon@GMAIL.COM"
        user     = get_user_model().objects.create_user(email=email,password="test123")

        self.assertEqual(user.email,email.lower()) 

    def test_user_email_invalid(self):
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None,password="test123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser("nebumathomkuttan@gmail.com","test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

        
