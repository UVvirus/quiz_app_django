from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("index page")

def detail(request,question_id):
    return HttpResponse("THe question is %s"% question_id)

def results(request,question_id):
    response="the answer is %s"
    return HttpResponse(response % question_id)


