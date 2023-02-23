from django.urls import include, path
from . import views

app_name = "messages"
urlpatterns = [

    path('<int:id>', views.MessageListView.as_view(), name='message_by_chat_id'),
    path('view/<int:id>', views.MessageDataView.as_view(), name="comment_data"), 
]