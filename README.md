# Python Testcontainer RabbitMQ

## Usage

```python
import pika
from testcontainer_python_rabbitmq import RabbitMQContainer


def test_rabbitmq():
    config = RabbitMQContainer()
    with config as container:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=container.get_container_host_ip(),
                port=container.get_amqp_port(),
                credentials=pika.PlainCredentials(username="guest", password="guest"),
            )
        )

        # do something...
```
