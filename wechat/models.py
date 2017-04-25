# coding=utf-8
from django.db import models


class HistoryMessage(models.Model):
    """
    保存历史消息
    """
    id = models.IntegerField(max_length=16)
    recipient = models.CharField(max_length=64, help_text='接受者')
    sender = models.CharField(max_length=64, help_text='发送者')
    content = models.TextField(max_length=2048, help_text="历史消息")
    create_time = models.DateField(auto_now=True)