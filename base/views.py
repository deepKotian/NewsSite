from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import Post, News, Contact
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    return render(request , 'index.html')

def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

def tournament(request):
    return render(request , 'tournament.html')

def contact(request):
    if request.method == 'POST':
        contact =Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.comment = comment
        contact.save()
        return HttpResponse("Thanks")
    else:
        return render(request , 'contact.html')

def blog(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts': allPosts}
    return render(request , 'blog.html', context)

def news(request):
    allNews = News.objects.all()
    print(allNews)
    context = {'allNews': allNews}
    return render(request , 'news.html', context)

def merch(request):
    return render(request , 'merch.html')

def chatroom(request):
    return render(request , 'chatroom.html')

def blogpost(request):
    return render(request , 'blogpost.html')

class create(CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'
   

def blogpost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    print(post)
    context = {'post': post}
    return render(request , 'blogpost.html', context)

def newspost(request, slug):
    news = News.objects.filter(slug = slug).first()
    print(news)
    context = {'news': news}
    return render(request , 'newspost.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("Success!")
            return redirect("/")
        else:
            messages.info(request,'Invalid cedentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Password not matching..')
            return redirect('signup')
           

    else:         
       return render(request, 'signup.html')


def logout(request):
   auth.logout(request)
   return redirect('/')

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'search.html', params)
  
 