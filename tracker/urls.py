from django.urls import path
from . import views
app_name="tracker"
urlpatterns=[
    path('item',views.add_item,name="items"),
    path('<int:id>/', views.delete, name='delete'),
    path('sortname',views.sortbyname,name="sname"),
path('sortprice',views.sortbyprice,name="sprice"),
path('sortdate',views.sortbydate,name="sdate"),
]



