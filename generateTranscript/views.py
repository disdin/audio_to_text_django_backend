from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def generateTranscript(request):
    if request.method == "POST":
        # json_data = {'output': "", 'img': ""}
        # return JsonResponse(json_data)
        return HttpResponse("I want to deposit Rs5000 in my account.")
