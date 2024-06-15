from django.urls import path
from . import views, API
from .API import api_views

urlpatterns = [
    path('', views.index, name='index'), # 메인페이지
    path('api/login', api_views.login) # API 로그인
]