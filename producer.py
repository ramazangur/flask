import pika, json

params = pika.URLParameters('amqps://wduxddha:8sylkVhSxgA2t4VAo8KATCrTC2UfbI4m@moose.rmq.cloudamqp.com/wduxddha')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)