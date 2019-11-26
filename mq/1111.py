# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""

# import pika
#
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
#
#
# # channel.queue_declare(queue='hello')
#
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#
# channel.basic_consume(queue='hello',on_message_callback=callback)
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

a = 'aaa/bbb/yz.xlsx'
import os

x = a.split('/')

y = '/'.join(x[:-1])
if y:
    assert os.path.isdir(y) == True

os.path.split()