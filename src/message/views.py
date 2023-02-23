from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            user=request.POST.get('user_name')
            email=request.POST.get('email')
            home_page=request.POST.get('home_page')
            text=request.POST.get('comment')
            chat_instance = Chat.objects.get(id=kwargs['id'])
            if not home_page:
                Message.objects.create(chat_id=chat_instance, user=user, email=email, text=text)
            elif home_page:
                Message.objects.create(chat_id=chat_instance, user=user, email=email, home_page=home_page, text=text)
            else:
                print('some problem')
            return JsonResponse({'message': 'success'})
        return JsonResponse({'message': 'Wrong request'})


# def messages_by_chat_id(request, id):
#     template = loader.get_template("specific_chat/message.html")
#     comments = Message.objects.filter(chat_id = id)
#     # paginator = Paginator(comments, 2) # Show 25 contacts per page.
#     page_num = request.GET.get('page', 1)
#     paginator = Paginator(comments, 2) # 6 employees per page
#     page_obj = paginator.get_page(page_num)
#     try:
#         page_obj = paginator.page(page_num)
#     except PageNotAnInteger:
#         # if page is not an integer, deliver the first page
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         # if the page is out of range, deliver the last page
#         page_obj = paginator.page(paginator.num_pages)
#     context = {
#         "page_obj": page_obj
#     }
#     # return render(request, "specific_chat/message.html", {'page_obj': page_obj})
#     return HttpResponse(template.render(context, request))
class MessageDataView(generic.View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template("specific_chat/message.html")
        try:
            if kwargs['sort'] == 'text':
                comments = Message.objects.filter(chat_id = kwargs['id']).order_by('text')
            elif kwargs['sort'] == 'name':
                comments = Message.objects.filter(chat_id = kwargs['id']).order_by('name')
         
                
        except:
            comments = Message.objects.filter(chat_id = kwargs['id'])
        context = {
            "chat_id": kwargs['id'],
            "commnt_list": comments
        }

        return HttpResponse(template.render(context, self.request))

