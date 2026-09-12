from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_url_exists_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
        
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')