#coding=utf8
import requests
import itchat

KEY = 'd2d6c527ea374504bfc88edf7e0a1d21'

def get_response(msg):

    apiUrl = 'http://api.turingos.cn/turingos/api/v2'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()

        return r.get('text')

    except:

        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
