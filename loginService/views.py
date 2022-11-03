from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
import hashlib

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

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_id = data['user_id']
        obj = Account.objects.get(user_id=search_id)
        token = hashlib.sha256()
        token.update(obj.password.encode())
        obj.token = token.hexdigest()
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
        token = request.POST['token']
        status = request.POST['work_status']
        obj = Account.objects.get(user_id=token)
        if status == 'work' or status == 'finish' or status == 'pause' or status == 'home':
            obj.work_status = request.POST['work_status']
        else:
            return JsonResponse(status=400)
