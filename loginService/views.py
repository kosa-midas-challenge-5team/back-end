from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
import hashlib
import time

@csrf_exempt
def test(request):
    return HttpResponse("test")

@csrf_exempt
def account_list(request):
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if Account.objects.filter(user_id=data['user_id']).exists():
            return HttpResponse(status=409)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def account(request, pk):

    obj = Account.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AccountSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
    
    else:
        return HttpResponse(status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_id = data['user_id']
        obj = Account.objects.get(user_id=search_id)
        token = hashlib.sha256()
        token.update(obj.password.encode())
        obj.token = token.hexdigest()
        obj.save()
        if obj.admin:
            if data['password'] == obj.password:
                req = {
                    "auth" : "admin",
                    "token" : obj.token
                }
                return JsonResponse(req, status=200)
            else:
                return JsonResponse(status=400)
        else:
            if data['password'] == obj.password:
                req = {
                    "auth" : "user",
                    "token" : obj.token
                }
                return JsonResponse(req, status=200)
            else:
                return JsonResponse(status=400)

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        token = data['token']
        obj = Account.objects.get(token=token)
        status = data['work_status']
        if status == 'work':
            obj.work_status = data['work_status']
            obj.work_time = (time.time())
        elif status == 'finish':
            obj.work_status = data['work_status']
            obj.work_time = (int(time.time()) - obj.work_time)
        elif status == 'pause' or status == 'home':
            obj.work_status = data['work_status']
        obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def admin(request):
    if request.method == 'GET':
        token = request.GET['token']
        obj = Account.objects.get(token=token)
        if obj.admin:
            sort_type = request.GET['sort_type']
            if sort_type == 'name':
                name = request.GET['user_id']
                query_set = Account.objects.filter(name=name)
                serializer = AccountSerializer(query_set, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif sort_type == 'group':
                name = request.GET['user_id']
                query_set = Account.objects.filter(group=name)
                serializer = AccountSerializer(query_set, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif sort_type == 'work':
                query_set = Account.objects.filter(work_status='work')
                serializer = AccountSerializer(query_set, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif sort_type == 'pause':
                query_set = Account.objects.filter(work_status='pause')
                serializer = AccountSerializer(query_set, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif sort_type == 'home':
                query_set = Account.objects.filter(work_status='home')
                serializer = AccountSerializer(query_set, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif sort_type == 'finish':
                query_set = Account.objects.filter(work_status='finish')
                serializer = AccountSerializer(query_set, many=True)
                return JsonResponse(serializer.data, safe=False)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def modify(request):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        token = data['token']
        obj = Account.objects.get(token=token)
        if obj.admin:
            user_id = data['user_id']
            obj = Account.objects.get(user_id=user_id)
            if 'name' in data:
                obj.name = data['name']
            if 'group' in data:
                obj.group = data['group']
            if 'admin' in data:
                obj.admin = data['admin']
            obj.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)