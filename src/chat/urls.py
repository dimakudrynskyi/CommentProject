from django.urls import include, path
from . import views

urlpatterns = [

    #Pages
    path('', views.ChatListView.as_view(), name='all_chats'),
   
]