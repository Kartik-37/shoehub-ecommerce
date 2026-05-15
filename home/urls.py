
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('gym sneakers',views.gymsneakers,name="gym sneakers"),
    path('hike sneakers',views.hikesneakers,name="hike sneakers"),
    path('work sneakers',views.worksneakers,name="work sneakers"),
    path('chuck sneakers',views.chucksneakers,name="chuck sneakers"),
    path('contact',views.contact,name="contact"),
    path('men',views.man,name="man"),
    path('women',views.women,name="women"),
    path('kid',views.kid,name="kid"),
    path('login_view',views.login_view,name="login_view"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('register',views.register,name="register"),
    path('detail/<int:id>',views.detail,name="detail"),
    path('cart',views.cart,name="cart"),
    path('cart1/<int:id>',views.cart1,name="cart1"),
    path('delcart/<int:id>',views.delcart,name="delcart"),
    path('account',views.account,name="account"),
    path('edit',views.edit,name="edit"),
    path('payment',views.payment,name="payment"),
    path('invoice',views.invoice,name="invoice"),
    path('admindesk',views.admindesk,name="admindesk"),
    path('adminuser',views.adminuser,name="adminuser"),
    path('adminorder',views.adminorder,name="adminorder"),
    path('adminproduct',views.adminproduct,name="adminproduct"),
]
