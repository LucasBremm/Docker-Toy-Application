import pika
import sys
from datetime import datetime
import time
import random
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='temp', exchange_type='topic')

while(True):

    now = datetime.now()
    
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    message = {
        'id':random.randint(1, 5),
        'value':random.randint(0, 40),
        'time':date_time,
        'type':'temperatura'
    }

    channel.basic_publish(exchange='temp', routing_key='values', body=json.dumps(message))

    time.sleep(5)

connection.close()