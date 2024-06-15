from django.shortcuts import render
from django.db.models import Q # 검색 필터
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, get_list_or_404
# from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from ..models import Account as UserModel
import requests
import json
import time
import re
from datetime import datetime, timedelta
# Create your views here.



@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            print("여기 데이터요", data)
            user = authenticate(request, username=username, password=password)
            
            if user:
                return JsonResponse({"status" : True, "msg" : "로그인성공"}, status=200)
            
            else:
                print("로그인실패")
                return JsonResponse({"status" : False, "msg" : "로그인실패"}, status=400)
        except Exception as e:
            print("로그인 에러 발생", e)
            return JsonResponse({"status" : False, "msg" : "로그인 에러발생"}, status=400) 
    else:
        return JsonResponse({"status" : False, "msg" : "호출 메소드 에러"}, status=400)