import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

rabbit_message = 'Hello World!'

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=rabbit_message)

print("%s message was sent!" % rabbit_message)

connection.close()
