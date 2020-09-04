from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def video(request):
    return render(request, 'video.html')

def photography(request):
    return render(request, 'photography.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def join(request):
    return render(request, 'join.html')

def signupdone(request):
    return render(request, 'signupdone.html')

def board(request):
    return render(request, 'board.html')

def contents(request):
    return render(request, 'contents.html')

def mypage(request):
    return render(request, 'mypage.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
