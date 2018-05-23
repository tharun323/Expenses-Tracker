from django.test import TestCase
from tracker.models import Item
from django.utils import timezone
from tracker.forms import *
import datetime
from django.test import Client
from django.shortcuts import render,redirect,reverse
class ItemViewTests(TestCase):

    def test_signup(self):
        response = self.client.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response.status_code, 200)

    def test_display(self):
        response = self.client.get("http://127.0.0.1:8000/display/")
        self.assertEqual(response.status_code, 200)

    def test_sortname(self):
        response = self.client.get("http://127.0.0.1:8000/sortname/")
        self.assertEqual(response.status_code, 200)

    def test_sortprice(self):
        response = self.client.get("http://127.0.0.1:8000/sortprice/")
        self.assertEqual(response.status_code, 200)

    def test_sdate(self):
        response = self.client.get("http://127.0.0.1:8000/sortdate/")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        p=Client()
        response = p.post('http://127.0.0.1:8000/accounts/login/',{'username': "tharunreddy", 'password': "Tharun@django"})
        self.assertNotEquals(response.status_code, 302)

    def test_logout(self):
        p=Client()
        response = p.post('http://127.0.0.1:8000/accounts/logout/')
        response = c.get('/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 302)

class ItemModelTest(TestCase):

    def create_item(self,name="television",price=1200):
        return Item.objects.create(name=name,price=price,created_at=timezone.now())

class UserFormTest(TestCase):

    def test_valid_form(self):
        w = Item.objects.create(name='bike', price=10000)
        data = {'username':"tharun", 'email':"atkr323@gmail.com",'password1':"Chintu123",'password2':"Chintu123"}
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Item.objects.create(name='bike', price=10000)
        data = {'username': "tharun", 'email': "atkr323@gmail.com", 'password1': "Chin123", 'password2': "Chintu123"}
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())

class ItemModelFormTest(TestCase):

    def test_valid_form(self):
        w = Item.objects.create(name='bike', price=10000,image='images/bicycle.png')
        data = {'name':"Bike",'price':10000}
        form = ItemModelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Item.objects.create(name='bike', price=10000)
        data = {'name': "Bike",}
        form = ItemModelForm(data=data)
        self.assertFalse(form.is_valid())