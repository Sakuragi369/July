# coding=utf-8
from django.shortcuts import render
import itchat
import re
import time

"""
基于itchat包，对微信进行数据分析，好友数量、男女比例、被拉黑好友检测...
"""

def wechat_login():
    itchat.auto_login(hotReload=True)


def wechat_friends_rat():
    wechat_login()
    friends = itchat.get_friends(update=True)[0:]
    total = len(friends[1:])
    man = woman = other = 0
    for i in friends[1:]:
        sex = i['Sex']
        if sex == 1:
            man += 1
        elif sex == 2:
            woman += 1
        else:
            other += 1

    return {
        "total": total,
        "man": man,
        "woman": woman,
        "other": other
    }


def wechat_signature():
    wechat_login()
    friends = itchat.get_friends(update=True)[0:]
    tList = []
    for i in friends:
        signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("1f\d.+")
        signature = rep.sub("", signature)
        tList.append({i["NickName"]: signature})
    return tList


# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])

if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()


if __name__ == "__main__":
    # result = wechat_friends_rat()
    # result = wechat_signature()
    # print result
    wechat_login()
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()