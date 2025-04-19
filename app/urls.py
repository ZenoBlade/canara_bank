from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("1",views.create,name='create'),
    path("2",views.pingen,name='pingen'),
    path("3",views.deposit,name='deposit'),
    path("4",views.withdraw,name='withdraw'),
    path("5",views.balance,name='balance'),
    path("6",views.acctransfer,name='acctransfer'),
]