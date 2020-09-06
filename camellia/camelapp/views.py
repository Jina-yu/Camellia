from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import auth
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def video(request):
    return render(request, 'video.html')

def photography(request):
    return render(request, 'photography.html')

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['name'], 
            password=request.POST['password'],
            email=request.POST['address'],
            birth=request.POST['birth'],
            message=request.POST['message']
            )
        auth.login(request, user)
        return redirect('signupdone')
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'mypage.html',{'user':user})
        else :
            return render(request, 'signin.html', {'error' : '아이디나 비밀번호가 틀렸습니다.'})
    else :
        return render(request, 'signin.html')


def join(request):
    return render(request, 'join.html')

def signupdone(request):
    return render(request, 'signupdone.html')

def board(request):
    content = Board.objects.all()
    date= Board.objects.all()
    title= Board.objects.all()
    type=Board.objects.all()
    paginator = Paginator(content,10)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request, 'board.html', {'content':content, 'date':date, 'type':type, 'post': post})

def contents(request, pk):
    if request.user.is_authenticated:
        content = Board.objects.filter(pk=pk)
        return render(request, 'contents.html', {'content':content})
    else:
        return redirect('board')
    # date= Board.objects.filter(pk=pk)
    # title= Board.objects.filter(pk=pk)
    # type=Board.objects.filter(pk=pk)

def mypage(request, pk):
    user = get_object_or_404(User,pk=pk)
    if request.user.is_authenticated:
        return render(request,'mypage.html',{'user':user})
    else:
        return redirect('signin')


def logout(request):
    auth.logout(request)
    return redirect('index')




def create(request, pk):
    user = get_object_or_404(User,pk=pk)
    if request.method=='POST':
        create=Board()
        create.user = request.user
        create.title = request.POST['title']
        create.content = request.POST['content']
        create.type = request.POST['type']
        create.call = request.POST['call']
        create.save()  #리뷰생성
        return redirect('board')

def delete_content(request):
    deletecontent = request.POST['content_id'] # 삭제 버튼을 눌렀을 때 content_id 를 받아옴
    content = Board.objects.get(id=deletecontent) # models 의 Board 중 id 가 같은 것을 가져옴
    content.delete() # 삭제
    return redirect('board')
