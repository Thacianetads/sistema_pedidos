import pika
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, 
'/', pika.PlainCredentials('user','pass')))
channel = connection.channel()
channel.queue_declare(queue='fila')

def callback(ch, method, properties, body):
    message = body.decode()
    nome = message.get("nome")
    produto = message.get("produto")
    valor = message.get("valor")
    
    print(f"Pedido recebido: {nome} - {produto} (R$ {valor})")

channel.basic_consume(queue="fila", on_message_callback=callback, auto_ack=True)
print("Aguardando novos pedidos na fila...")
channel.start_consuming()