import time

import common


def callback(ch, method, properties, body):
    print("Received:", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    time.sleep(0.1)


if __name__ == '__main__':
    channel = common.get_channel()
    queue_name = common.queue_name

    # set consume_config
    channel.basic_consume(queue=queue_name,
                          on_message_callback=callback) # default auto_ack=False
    # start consuming
    channel.start_consuming()
