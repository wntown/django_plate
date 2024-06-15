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
from .models import Account as UserModel
import requests
import json
import time
import re
from datetime import datetime, timedelta
# Create your views here.


def index(request):
    return HttpResponse("메인 홈페이지")