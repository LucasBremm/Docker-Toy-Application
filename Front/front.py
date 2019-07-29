import requests, json, pika, time
from threading import Thread, Lock
from flask import Flask, jsonify

class Dados:
    dados = []

    def __init__(self):
        self.lock = Lock()
    
    def insert(self, dados):
        self.lock.acquire()
        try:
            self.dados.append(dados)
        finally:
            self.lock.release()
    
    def getInfo(self, id):
      self.lock.acquire()
      try:
         dado = []
         for d in self.dados:
            if(d['id'] == id):
               dado.append(d)
         return dado
      finally:
         self.lock.release()

def conn():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.exchange_declare(exchange='temp', exchange_type='topic')

    result = channel.queue_declare(queue='values')
    queue_name = result.method.queue

    channel.queue_bind(exchange='temp', queue=queue_name)

    def callback(ch, method, properties, body):
        dados.insert(json.loads(body.decode()))

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

dados = Dados()

t = Thread(target = conn)
t.start()

url = 'http://192.168.0.105:2000/info/'

app = Flask(__name__)

@app.route('/info/<int:id>')
def entradas(id):
   entrada = id
   
   req = requests.get(url + str(entrada))

   js = json.loads(req.content.decode())

   nome = js['nome']

   js = dados.getInfo(js['id']) 
   
   js.append({'nome':nome})

   return jsonify(js)

if __name__ == '__main__':
   app.run(threaded = False, host = '0.0.0.0', port = 3000)

# while(True):
#     entrada = input("#")

#     req = requests.get('http://127.0.0.1:2000/info/' + entrada)

#     js = json.loads(req.content.decode())

#     js = dados.getInfo(js) 

#     print(js)

