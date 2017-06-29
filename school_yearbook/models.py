# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from utils.common_tools import create_uuid
import datetime

# Create your models here.

IS_VALID = (
    ('0', 'invalid',),
    ('1', 'valid',),
)


class User(models.Model):
    """
    用于同学录登录
    账号密码提前录入
    """
    LOCKED_VALID = (
        (0, '冻结',),
        (1, '正常',),
    )

    id = models.CharField('user id', max_length=36, primary_key=True,
                          default=create_uuid(), help_text='user id')
    name = models.CharField('user name', max_length=75, help_text='user name.', unique=True)
    mobile = models.CharField('mobile', max_length=20, help_text='Mobile. No.')
    email = models.CharField('email', max_length=75, help_text='Email.')
    wechat = models.CharField('WeChat', max_length=75, help_text='WeChat.')
    address = models.CharField('address', max_length=255, blank=True, null=True,
                               help_text=u'home address.')
    update_time = models.DateTimeField('update time', blank=True, null=True, default=datetime.datetime.now,
                                       help_text='update time.')
    is_valid = models.BooleanField(choices=IS_VALID, default=True)
    locked = models.BooleanField(choices=LOCKED_VALID, default=1)
    ext_data = models.TextField(default='{}', null=False, help_text="extend data")

    class Meta:
        db_table = 'account_user'


class Label(models.Model):
    content = models.CharField('label content', max_length=36, help_text='label content')
    create_time = models.DateTimeField('create_time', blank=True, null=True, default=datetime.datetime.now,
                                       help_text='create_time.')
    is_valid = models.BooleanField(choices=IS_VALID, default=True)


