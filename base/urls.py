from django.urls import path
from base import views
from django.conf.urls.static import static
from django.conf import settings
from .views import create

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
    path('chatroom/', views.chatroom, name='chatroom'),
    path('logout/', views.logout, name='logout'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('blogpost/<str:slug>/', views.blogpost, name="blogpost"),
    path('newspost/', views.newspost, name='newspost'),
    path('newspost/<str:slug>/', views.newspost, name="newspost"),
    path('search/', views.search, name='search'),
    path('create/', create.as_view(), name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

