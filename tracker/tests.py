from django.test import TestCase
from tracker.models import Item
from django.utils import timezone
from tracker.forms import *
import datetime

class ItemViewTests(TestCase):

    def test_signup(self):
        response = self.client.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response.status_code, 200)

    def test_item(self):
        response = self.client.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response.status_code, 200)

    def test_display(self):
        response = self.client.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response.status_code, 200)

    def test_sortname(self):
        response = self.client.get("http://127.0.0.1:8000/sortname/?")
        self.assertEqual(response.status_code, 200)

    def test_sortprice(self):
        response = self.client.get("http://127.0.0.1:8000/sortprice/?")
        self.assertEqual(response.status_code, 200)

    def test_sdate(self):
        response = self.client.get("http://127.0.0.1:8000/sortdate/?")
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        response = self.client.get("http://127.0.0.1:8000/accounts/login")
        self.assertEqual(response.status_code, 301)

    def test_logout(self):
        response = self.client.get("http://127.0.0.1:8000/accounts/logout")
        self.assertEqual(response.status_code, 301)

    def test_update(self):
        response = self.client.get("http://127.0.0.1:8000/<int:id>/edit/")
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        response = self.client.get("http://127.0.0.1:8000/<int:id>/")
        self.assertEqual(response.status_code, 200)


class ItemModelTest(TestCase):

    def create_item(self,name="television",price=1200):
        return Item.objects.create(name=name,price=price,created_at=timezone.now())

    def test_item_creation(self):
        w=self.create_item()
        self.assertTrue(isinstance(w,Item))
        self.assertEqual(w.__str__(),w.name)

    def test_was_published_now(self):
        time=timezone.now()+ datetime.timedelta(days=20)
        future_item=Item(created_at=time)
        self.assertIs(future_item.was_published_now(),False)

    def test_price(self):
        w=self.create_item()
        self.assertTrue(isinstance(w,Item))
        self.assertIs(w.test_for_price(),w.price)


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