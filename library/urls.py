from django.urls import path
from .views import *
from . import views
urlpatterns = [

    path('register', my_regestration, name='registration'),
    path('login', mylogin, name='login'),
    path('logout', mylogout, name='logout'),
    path('add', add, name='add'),
    path('list', list, name='list'),
    path('edit/<pk>',Update.as_view(),name='edit'),
    path('delete/<pk>',Delete.as_view(),name='delete'),

]