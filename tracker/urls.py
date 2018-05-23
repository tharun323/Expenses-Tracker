from django.urls import path,include
from . import views
from django.contrib.auth.views import logout_then_login

app_name="tracker"
urlpatterns=[

    path('signup/',views.signup,name="signup"), # URL for  signup page

    path('item/',views.add_item,name="items"),  # URL for Adding items

    path('display/',views.display,name="display"), #URL for displaying

    path('<int:id>/', views.delete, name='delete'), #URL for deleting

    path('sortname/',views.sortbyname,name="sname"), #URL for sorting by name page

    path('sortprice/',views.sortbyprice,name="sprice"),#URL for sorting by price page

    path('sortdate/',views.sortbydate,name="sdate"),#URL for sorting by date page

    path('<int:id>/edit/',views.update,name="update"),#URL for editing page

    path('accounts/', include('django.contrib.auth.urls'),name="login"),#URL for Login

    path('accounts/logout', include('django.contrib.auth.urls'), name="logout"),#URL for logout
]





