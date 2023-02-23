from django.urls import include, path
from . import views

urlpatterns = [

    #Pages
    path('', views.ChatListView.as_view(), name='all_chats'),
    path('chat/create', views.CreateChatView.as_view(), name='create_chat'),
   
]