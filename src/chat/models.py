from django.db import models

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=355, null=False, default="")

    class Meta:
        ordering = ('name', )
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self) -> str:
        return "chat_id - {0} chat_name - {1}".format(self.id, self.name)