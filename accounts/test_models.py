from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestMyProfileModel(TestCase):

    def create_myprofile(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(position='PM', personality='socializer', owner = user)
        return MyProfile.objects.create(position=position,
                                        personality = personality,
                                        owner = owner)
    
    def test_create_myprofile(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(position='PM', personality='socializer', owner = user)
        self.assertTrue(isinstance(myprofile , MyProfile))
    
    
    def test_myprofile_position_defaults_to_coder(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(personality='socializer', owner = user)
        myprofile.save()
        self.assertEqual(myprofile.position, "Coder")
        self.assertEqual(myprofile.personality, "socializer")
        
    def test_myprofile_as_a_string(self):
        user = User.objects.create_user(username='Tester', password='password')
        self.client.login(username='Tester', password='password')
        myprofile = MyProfile.objects.create(personality='socializer', owner = user)
        self.assertEqual("Tester", str(myprofile))
        
        
class TestPositionModel(TestCase):        
    
    def create_position(self):
        position = Position.objects.create(name='Tester')
        return Position.objects.create(name=name)
    
    def test_create_position(self):
        position = Position.objects.create(name='Tester') 
        self.assertTrue(isinstance(position , Position))
        
    def test_position_as_a_string(self):
        position = Position.objects.create(name='Tester') 
        self.assertEqual("Tester", str(position))
        
        
class TestPersonalityModel(TestCase):        
    
    def create_personality(self):
        personality = Personality.objects.create(name='Tester')
        return Personality.objects.create(name=name)
    
    def test_create_position(self):
        personality = Personality.objects.create(name='Tester') 
        self.assertTrue(isinstance(personality , Personality))
        
    def test_position_as_a_string(self):
        personality = Personality.objects.create(name='Tester') 
        self.assertEqual("Tester", str(personality))        