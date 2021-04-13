from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(name = 'kigali')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

     # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)  

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.flower= Image(name = 'flower', image_url ='https://images.pexels.com/photos/462118/pexels-photo-462118.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', description ='rose flower')

         # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.flower,Image))


       
     # Testing Save Method
    def test_save_method(self):
        self.flower.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)  