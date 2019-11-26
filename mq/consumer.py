# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""
# import pika
# x = pika.ConnectionParameters('localhoost',port=8080)
# connection = pika.BlockingConnection(x)
# channel = connection.channel()
# channel.queue_declare('hello')
#
# def call_back(ch,method,properties,body):
#     print(ch,'--------')
#     print(method,'+++++++')
#     print(properties,'*********')
#     print(body,'&&&&&&&&&&&&&77')
#
# channel.basic_consume(
#     call_back,queue='hello',no_ack=True
# )
# channel.start_consuming()


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.exchange_declare(exchange='logs', exchange_type='fanout',durable=True,auto_delete=False,passive=True)
result = channel.queue_declare('',exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
channel.basic_consume(queue_name,callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
