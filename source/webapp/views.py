import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, context=None, template_name="index.html")



@csrf_exempt
def api_example(request, *args, **kwargs):
    request_data = None

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        a = data.get("A")
        b = data.get("B")
        result = int(a) + int(b)
        answer = json.dumps(result)
        response = HttpResponse(answer)
        return response


@csrf_exempt
def subtract(request, *args, **kwargs):
    request_data = None

    if request.method == "POST":
        data = json.loads(request.body)
        a = data.get("A")
        b = data.get("B")
        result = int(a) - int(b)
        answer = json.dumps(result)
        response = HttpResponse(answer)
        return response


@csrf_exempt
def multiply(request, *args, **kwargs):
    request_data = None

    if request.method == "POST":
        data = json.loads(request.body)
        a = data.get("A")
        b = data.get("B")
        result = int(a) * int(b)
        if result != 0:
            answer = json.dumps(result)
        else:
            answer = json.dumps("MATHERFUCKER")
        response = HttpResponse(answer)
        return response


@csrf_exempt
def divide(request, *args, **kwargs):
    request_data = None

    if request.method == "POST":
        data = json.loads(request.body)
        a = data.get("A")
        b = data.get("B")
        result = 0

        if int(a) > int(b):
            try:
                result = int(a) / int(b)
            except: ZeroDivisionError()
        elif int(a) < int(b):
            try:
                result = int(b) / int(a)
            except:
                ZeroDivisionError()
        if result != 0:
            answer = json.dumps(result)
        else:
            answer = json.dumps("MATHERFUCKER")
        response = HttpResponse(answer)
        return response

# Create your views here.
