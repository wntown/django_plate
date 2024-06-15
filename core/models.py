from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import datetime, timedelta
import uuid
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError("아이디를 입력 해주세요")
        
        if not name:
            raise ValueError("이름을 입력 해주세요")

        if not password:
            raise ValueError("비밀번호를 입력 해주세요")

        user = self.model(
            username = username,
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username, name, password):
        user = self.create_user(
            username = username,
            name = name,
            password = password,
            
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    objects             =       MyAccountManager()
    username            =       models.CharField(max_length=32,verbose_name='아이디', null=False ,blank=False, unique=True)
    useremail           =       models.EmailField(max_length=128,verbose_name='이메일', null=False ,blank=False, unique=True)
    phoneNumberRegex    =       RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone               =       models.CharField(validators = [phoneNumberRegex], max_length = 11, verbose_name='전화번호', unique = True, null=False, blank=False)
    name                =       models.CharField(max_length=10, verbose_name='사용자 이름', null=False ,blank=False)
    password            =       models.CharField(max_length=256, verbose_name='비밀번호', null=False, blank=False)
    money_point         =       models.IntegerField(default=0, verbose_name='보유 포인트')
    is_active           =       models.BooleanField(default=True, verbose_name='사용가능 여부')
    is_admin            =       models.BooleanField(default=False, verbose_name='어드민 여부')
    is_staff            =       models.BooleanField(default=False, verbose_name='스텝여부 여부')
    is_superuser        =       models.BooleanField(default=False, verbose_name='슈퍼관리자 여부')
    last_login          =       models.DateTimeField(auto_now_add=True ,verbose_name="마지막 로그인 시간")
    date_joined         =       models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    uuid                =       models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=100, verbose_name='UUID')
    USERNAME_FIELD      =       'username' # username 으로 사용할 필드
    REQUIRED_FIELDS     =       ['name',] # 필수로 넣어야 하는 필드 (비밀번호 같은것들은 기본적으로 들어감)
    

    # def total_count(self):    
    #     return AAAA.objects.filter(create_user=self.pk).count()
    # total_count.short_description = "총 갯수"
    
    class Meta:
        verbose_name = '고객 리스트'
        verbose_name_plural = '고객 리스트'
