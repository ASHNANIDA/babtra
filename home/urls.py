from django.urls import path
from . import views
urlpatterns = [
    
    path('main/',views.main),
    path('index/',views.index,name='index'),
    path('about/',views.about),
    path('sample/',views.sample ,name='sample'),
    path('payment/',views.payment,name='payment'),
    path('ecom/',views.ecom),
    path('home/',views.home),
    path('login/',views.login,name='login'),
    path('log/',views.log,name='log'),
    path('ajaxb9/',views.ajaxb9,name='ajaxb9'),
    path('msg1/',views.msg1,name='msg1'),
    path('msg3/',views.msg3,name='msg3'),
    path('new/',views.fnnew,name='new'),
    path('old/',views.old,name='old'),


]