from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('tournament/', views.tournament, name='tournament'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('merch/', views.merch, name='merch'),
    path('chatroom/', views.chatroom, name='chatroom'),
    path('logout/', views.logout, name='logout'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('blogpost/<str:slug>/', views.blogpost, name="blogpost"),
    path('search/', views.search, name='search'),
]