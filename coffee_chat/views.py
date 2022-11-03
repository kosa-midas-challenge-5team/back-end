from django.views.decorators.csrf import csrf_exempt
from .models import Application
from .serializers import Serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def application_list(request):
    if request.method == 'GET':
        application = Application.objects.all()
        serializer = Serializers(application, many =True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def application_write(request, pk):
    obj = Application.objects.get(pk=pk)
    if request.method == 'GET':
        serializers = Serializers(obj)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = Serializers(obj, data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)