import pika, json

params = pika.URLParameters(
    'amqps://zbrsberv:vYxG0wUrodhtbQTdoYyH62KX-vG3O4qz@jackal.rmq.cloudamqp.com/zbrsberv')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)