from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect
from .models import Chat

# Create your views here.


class ChatListView(generic.ListView):
    model = Chat

    context_object_name = 'chat_list'   #name for the list as a template variable
    queryset = Chat.objects.all() 
    template_name = 'chat/all_chats.html'  # Specify template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ChatListView, self).get_context_data(**kwargs)
        return context

class CreateChatView(generic.View):
  
    def post(self, request, **kwargs):
        print('test')
        new_chat_name = request.POST['chat_name']
        print(request.POST['chat_name'])
        new_chat = Chat.objects.create(name=new_chat_name)
        print("finish")
        return redirect('all_chats')