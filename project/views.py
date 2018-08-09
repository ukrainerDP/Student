from django.shortcuts import render

from django.http import HttpResponse

from .models import People, Store, Check



def index(request):
    return HttpResponse('HttpResponse')

def general(request,question_id): 
    return HttpResponse(" Функция general. {}.".format(question_id))

def results(request,question_id): 
    return HttpResponse(" Функция results. {}.".format(question_id))
 
def detail(request,question_id):
    people = People.objects.get(id=question_id)
    return HttpResponse(people.full_name)


