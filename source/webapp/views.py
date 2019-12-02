# from django.shortcuts import render
# import json
# from datetime import datetime
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt



# @csrf_exempt
# def json_echo_view(request, *args, **kwargs):
#     answer = {
#         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         'method': request.method,
#     }
#     answer_as_json = json.dumps(answer)
#     response = HttpResponse(answer_as_json)
#     response['Content-Type'] = 'application/json'
#     return response

import json
from datetime import datetime
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

    # elif request.method == "GET":
    #     if request.body:
    #         request_data = json.loads(request.body)
    #     data = {
    #         'method': request.method,
    #         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #         'content': request_data
    #     }
    #     print(data)
    #     return JsonResponse(data)

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

    # elif request.method == "GET":
    #     if request.body:
    #         request_data = json.loads(request.body)
    #     data = {
    #         'method': request.method,
    #         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #         'content': request_data
    #     }
    #     print(data)
    #     return JsonResponse(data)

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

    # elif request.method == "GET":
    #     if request.body:
    #         request_data = json.loads(request.body)
    #     data = {
    #         'method': request.method,
    #         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #         'content': request_data
    #     }
    #     print(data)
    #     return JsonResponse(data)

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

    # elif request.method == "GET":
    #     if request.body:
    #         request_data = json.loads(request.body)
    #     data = {
    #         'method': request.method,
    #         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #         'content': request_data
    #     }
    #     print(data)
    #     return JsonResponse(data)
# Create your views here.
