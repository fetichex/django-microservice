import os
import django
import pika
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_ms.settings')
django.setup()

from products.models import Product

params = pika.URLParameters(
    'amqps://zbrsberv:vYxG0wUrodhtbQTdoYyH62KX-vG3O4qz@jackal.rmq.cloudamqp.com/zbrsberv')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, propeties, body):
    print('RECEIVED IN ADMIN')
    id = json.loads(body)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('product likes increased!')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print('CONSUMING')

channel.start_consuming()

channel.close()
