# Expenses-Tracker 
### A tool to keep track of all your expenses 


- The user will be able to create account and login

- The user will be able to add, update and delete expenses with expense name, total price, upload image


- The user will be able to see the list of expenses along with total expenses

- The user will be able to filter and sort expenses by name, price, image availability, created date

### Installation 

(this installation assumes that you have a github account )

**install python 3.0** 
 
**install Django 2.0** (using 'pip install django~=2.0' )

 
 Open command prompt and move to your required location then,

 Download by clicking green button of rightside top portion or Clone the repository by using 
 `git clone https://github.com/tharun323/Expenses-Tracker.git` and clone to desktop. 

 using command promnt 'cd *path-to-repository*' , change directory to **Website**

 Enter `python manage.py runserver`
 
 `python manage.py migrate`  ( to create database tables )
 
 `python manage.py makemigrations` ( to save the changes )

 Open chrome and enter the URL `http://127.0.0.1:8000/signup`.

 Create an account and start using.

 ### Testing :
 
 ( All the required settings for tests are made in website/settings.py )
 
 (Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloadsl) for python-testing in google chrome  , and    copy its absolute path in *EndToTndTest line no : 86 in tests.py* .( this testing assumes that the OP is using windows as the OS)
 
 install Selenium using `pip install selenium`
 
 install Django-nose using `pip install django-nose`

 install coverage using `pip install coverage`

 move to  `.../tracker/tests.py` and under `def EndToEndTest():` edit the username ,password ,email as mentioned in the script
 
 To Test the app , move to root directory of the project and runserver using `python manage.py runserver` then

 open another command prompt , move to root directory and run `python manage.py test tracker` to test the app.

 

 
 
 
