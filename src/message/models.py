from django.db import models
from src.chat.models import Chat

# Create your models here.


class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.DO_NOTHING, related_name="chat_id", null=True)
    user = models.CharField(max_length=255, null=False, default="")
    text = models.TextField(null=False, default="")

    class Meta:
        ordering = ('user',)

    def __str__(self) -> str:
        return 'id - {0}, user - {1}'.format(self.id, self.user)