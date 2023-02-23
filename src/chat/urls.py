from django.urls import include, path
from . import views
app_name = "chat"
urlpatterns = [

    #Pages
    path('', views.ChatListView.as_view(), name='all_chats'),
    path('chat/create', views.ChatListView.as_view(), name='create_chat'),
   
]