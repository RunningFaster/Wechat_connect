from django.shortcuts import render

# Create your views here.
def test(requset):
    return render(requset, 'test.html')

import hashlib


# 在视图函数中
def handle(request):
    try:
        # 先获取request
        # data = web.input()
        # if len(data) == 0:
        #     return "hello, this is handle view"
        signature = request.get("signature")  # 先获取加密签名
        timestamp = request.get("timestamp")  # 获取时间戳
        nonce = request.get("nonece")  # 获取随机数
        echostr = request.get("echostr")  # 获取随机字符串
        token = "yilukeji0955"  # 自己设置的token
        # 使用字典序排序（按照字母或数字的大小顺序进行排序）
        list = [token, timestamp, nonce]
        list.sort()

        # 进行sha1加密
        temp = ''.join(list)
        sha1 = hashlib.sha1(temp.encode('utf-8'))
        # map(sha1.update, list)
        hashcode = sha1.hexdigest()

        # 将加密后的字符串和signatrue对比，如果相同返回echostr,表示验证成功
        if hashcode == signature:
            return echostr
        else:
            return ""

    except Exception as e:
        return e



