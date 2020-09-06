from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    address = models.TextField(null = True) #회원 이메일 주소
    birth = models.DateField(null = True) #생년월일
    message = models.TextField(null = True) #하고싶은 말


class Board(models.Model):
    title =  models.CharField(max_length=100) #글 제목
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user') #글쓴이
    upload  = models.DateField(null = True, auto_now=True) #게시물 작성 날짜
    content  = models.TextField(null = True) #글 내용
    type = models.CharField(max_length=50) #문의종류
    call = models.CharField(max_length=50) #연락처