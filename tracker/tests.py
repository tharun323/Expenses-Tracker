from django.test import TestCase, LiveServerTestCase
from tracker.models import Item
from django.utils import timezone
from tracker.forms import *
import datetime
from django.test import Client
from django.shortcuts import render,redirect,reverse
from django.test import TestCase, LiveServerTestCase
from tracker.models import Item
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os,time

class ItemViewTests(TestCase):  # testing Views by checking response with status code

    def test_signup(self):      #signup page test
        response = self.client.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response.status_code, 200)

    def test_display(self):     #displaying items test
        response = self.client.get("http://127.0.0.1:8000/display/")
        self.assertEqual(response.status_code, 200)

    def test_sortname(self):    #sorting name test
        response = self.client.get("http://127.0.0.1:8000/sortname/")
        self.assertEqual(response.status_code, 200)

    def test_sortprice(self):   #sort price test
        response = self.client.get("http://127.0.0.1:8000/sortprice/")
        self.assertEqual(response.status_code, 200)

    def test_sdate(self):
        response = self.client.get("http://127.0.0.1:8000/sortdate/")
        self.assertEqual(response.status_code, 200)

    def test_login(self):        #on form submission test
        p=Client()
        response = p.post('http://127.0.0.1:8000/accounts/login/',{'username': "tharunreddy", 'password': "Tharun@django"})
        self.assertNotEquals(response.status_code, 302)

    def test_logout(self):       #logout page test
        p=Client()
        response = p.post('http://127.0.0.1:8000/accounts/logout/')
        response = p.get('/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 200)

class ItemModelTest(TestCase):    #testing models by creating an instance

    def create_item(self,name="television",price=1200):
        return Item.objects.create(name=name,price=price,created_at=timezone.now())

class UserFormTest(TestCase):      #Testing forms both Userform

    def test_valid_form(self):     #testing validation
        w = Item.objects.create(name='bike', price=10000)
        data = {'username':"tharun", 'email':"atkr323@gmail.com",'password1':"Chintu123",'password2':"Chintu123"}
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):   #invalid form testing using false details
        w = Item.objects.create(name='bike', price=10000)
        data = {'username': "tharun", 'email': "atkr323@gmail.com", 'password1': "Chin123", 'password2': "Chintu123"}
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())

class ItemModelFormTest(TestCase):  #testing Item form

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

#change the values of usename , password, email everytime you test here and in line no: 140 
class EndtoEndTest(LiveServerTestCase): #End to End testing using Selenium
    username = "test"                   #sample name
    email = "test@gmail.com"            #email
    password = "simple1234"             #and password

    driver = webdriver.Chrome('C:\\Users\\TharunReddy\\Desktop\\chromedriver') #load chrome driver from local system

    driver.get('http://127.0.0.1:8000/signup/') #Local host

    assert "Signup" in driver.title

    elem = driver.find_element_by_id("id_username") #finds elements by id and enter the data
    elem.send_keys(username)

    elem = driver.find_element_by_id("id_email")
    elem.send_keys(email)

    elem = driver.find_element_by_id("id_password1")
    elem.send_keys(password)

    elem = driver.find_element_by_id("id_password2")
    elem.send_keys(password)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)                     #Press enter key

    elem = driver.find_element_by_id("id_name")     #add items page , enter the credentials
    elem.send_keys("television")
    elem = driver.find_element_by_id("id_price")
    elem.send_keys(1000)
    driver.find_element_by_id("id_image").send_keys(os.getcwd() + "/speaker.jpg") #give path to image from root during testing
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    elem = driver.find_element_by_id("id_name")
    elem.send_keys("television")
    elem = driver.find_element_by_id("id_price")
    elem.send_keys(1000)
    driver.find_element_by_id("id_image").send_keys(os.getcwd() + "/speaker.jpg") #give path to image from root during testing
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    elem = driver.find_element_by_id("id_name")
    elem.send_keys("television")
    elem = driver.find_element_by_id("id_price")
    elem.send_keys(1000)
    driver.find_element_by_id("id_image").send_keys(os.getcwd() + "/speaker.jpg") #give path to image from root during testing
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_css_selector('.button.button2').click() #verify all filters
    time.sleep(2)
    driver.find_element_by_css_selector('.button.button5').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.button.button5').click()
    link = driver.find_element_by_link_text('Logout')
    time.sleep(2)
    link.click()
    link = driver.find_element_by_link_text('Login') #testing login page using creditials from Signup
    link.click()
    elem = driver.find_element_by_id("id_username") 
    elem.send_keys(username) 
    elem = driver.find_element_by_id("id_password")
    elem.send_keys(password)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    driver.close() #Closes the Chrome browser








