from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.template import loader

from .models import Message
from src.chat.models import Chat
from .forms import MessageForm, CapatchaForm
# Create your views here.



class MessageListView(generic.View):
    form_class = CapatchaForm
    def get(self, request, *args, **kwargs):
        context = {
            'chat_id': kwargs['id'], 
            'captcha_form': self.form_class
            }
        return render(request, "specific_chat/chat_by_id.html", context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print("KWARGS ---", kwargs)
        if request.method == "POST":
            form = CapatchaForm(request.POST)
            if form.is_valid():
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
            else:
                return JsonResponse({'message': 'problem with captcha'})
        return JsonResponse({'message': 'Wrong request'})

class MessageDataView(generic.View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template("specific_chat/message.html")
        try:
            if kwargs['sort'] == 'created_at':
                sort_by = "created_at"

            elif kwargs['sort'] == 'name':
                sort_by = "user"

            elif kwargs['sort'] == 'created_at_up':
                sort_by = "-created_at"

            elif kwargs['sort'] == 'name_up':
                sort_by = "-user"
            comments = self.get_coments(kwargs['id'], sort_by)
        except:
            comments = Message.objects.filter(chat_id = kwargs['id'])
        context = {
            "commnt_list": comments
        }

        return HttpResponse(template.render(context, self.request))

    @staticmethod
    def get_coments(chat_id, sort_by):
        """
            Function to get sorted comments by chat id.
            Use raw here to prevent SQL Injection.
        """
        if sort_by == "-created_at":
            raw = 'SELECT * FROM message_message WHERE chat_id_id = {0} ORDER BY "{1}" DESC'.format(chat_id, "created_at")
        elif sort_by == "-user":
            raw = 'SELECT * FROM message_message WHERE chat_id_id = {0} ORDER BY "{1}" DESC'.format(chat_id, "user")
        else:
            raw = 'SELECT * FROM message_message WHERE chat_id_id = {0} ORDER BY "{1}"'.format(chat_id, sort_by)
        comments = Message.objects.raw(raw)

        return comments

