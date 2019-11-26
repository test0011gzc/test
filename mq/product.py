# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""
# import pika
#
# connection= pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=8080))
#
# channel = connection.channel()
# channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='',routing_key='hello1',body='hello0 gzc')
# connection.close()
#
#
# print()
import pika
import sys

print(sys.argv)


# 建立连接
# 中间件和发送者在同一台机器，则host为localhsot
def aaa(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    print(connection)
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout',durable=True,auto_delete=False,passive=True)
    props = pika.BasicProperties(delivery_mode=2)
    channel.basic_publish(exchange='logs',  # 空串，定义默认的exchange
                          routing_key='',  # 队列名称需要routing_key指定
                          body=msg,properties=props)  # 需要发送的内容'Hello World!'
    print(" [x] Sent %s" % msg)
    connection.close()


while True:
    msg = input('请输入消息：')
    aaa(msg)

# class TestMQ:
#
#     def __init__(self):
#         pass
