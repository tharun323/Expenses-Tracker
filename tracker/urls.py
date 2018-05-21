from django.urls import path,include
from . import views
from django.contrib.auth.views import logout_then_login

app_name="tracker"
urlpatterns=[
    path('signup/',views.signup,name="signup"),
    path('item/',views.add_item,name="items"),
    path('display/',views.display,name="display"),
    path('<int:id>/', views.delete, name='delete'),
    path('sortname/',views.sortbyname,name="sname"),
    path('sortprice/',views.sortbyprice,name="sprice"),
    path('sortdate/',views.sortbydate,name="sdate"),
    path('<int:id>/edit/',views.update,name="update"),
    path('accounts/', include('django.contrib.auth.urls'),name="login"),
    path('accounts/logout', include('django.contrib.auth.urls'), name="logout"),
]





