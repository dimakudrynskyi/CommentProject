from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.template import loader

from .models import Message
from src.chat.models import Chat
from .forms import MessageForm
# Create your views here.



class MessageListView(generic.View):
    form_class = MessageForm
    def get(self, request, *args, **kwargs):
        context = {'chat_id': kwargs['id']}
        return render(request, "specific_chat/chat_by_id.html", context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print("KWARGS ---", kwargs)
        if request.method == "POST":
            user=request.POST.get('user')
            text=request.POST.get('comment')
            # form = self.form_class(request.POST)
            # form.save()
            # if form.is_valid():
            chat_instance = Chat.objects.get(id=kwargs['id'])
            Message.objects.create(chat_id=chat_instance, user=user, text=text)
            return JsonResponse({'message': 'success'})
            # return JsonResponse({'message': 'Field couldn\'t validate'}) 
        return JsonResponse({'message': 'Wrong request'})

class MessageDataView(generic.View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template("specific_chat/message.html")
        print(kwargs['id'])
        comments = Message.objects.filter(chat_id = kwargs['id'])
        print(comments)
        context = {
            "comment_list": comments
        }
        print('ALL COMMENT ', context)
        return HttpResponse(template.render(context, self.request))

class SaveComment(generic.View):

    def post(self, request, *args, **kwargs):
        form = MessageForm()