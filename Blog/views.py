# Create your views here.
from django.http import HttpResponse, Http404
import datetime
from django.template import loader, Context, RequestContext, Template
from django.shortcuts import render_to_response, redirect, get_object_or_404
from Blog.models import Message
import time
from datetime import date

def homepage(request):
   return render_to_response("index.html", {}, context_instance=RequestContext(request))
   
def messages(request):
    #load objects from Messages Table
    author_exists = 1
    message_exists = 1
    if request.method == "POST":
        new_message = request.POST.get('message')
        new_author = request.POST.get('author')
        new_date = date.today()
        author_exists = 0
        message_exists = 0
        if new_author:
            author_exists = 1
        if new_message:
            message_exists = 1
            if new_author:
                MESSAGE = Message(message=new_message, author=new_author, date=new_date)
                MESSAGE.save()
        
    message_list = Message.objects.order_by("-date")
    return render_to_response("messages.html", {'message_list':message_list, 'author_exists':author_exists, 'message_exists':message_exists}, context_instance=RequestContext(request))
