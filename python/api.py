from fastapi import FastAPI
import pika
import json

app = FastAPI()

@app.post("/send")
async def send_message(message: dict):
    connection = pika.BlockingConnection(pika.
    ConnectionParameters("localhost", 5672, '/', pika.
    PlainCredentials('user','pass')))
    channel = connection.channel()
    channel.queue_declare(queue="fila")
    channel.basic_publish(
        exchange="",
        routing_key="fila",
        body=json.dumps(message),
    )
    connection.close()
    return {
        "status": "sucesso",
        "message": "Seu pedido está sendo processado"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)