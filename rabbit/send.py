import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

rabbit_message = input("What's you message? ")

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=rabbit_message)

print(" [*] Message was sent '%s'" % rabbit_message)

connection.close()
