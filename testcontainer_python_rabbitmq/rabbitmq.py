import os

from requests import Response, exceptions, get, post
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_container_is_ready


class RabbitMQContainer(DockerContainer):
    def __init__(self, image="rabbitmq:3.9.22-management"):
        super(RabbitMQContainer, self).__init__(image)

        self.with_exposed_ports(5672, 15672)

    @wait_container_is_ready(exceptions.ConnectionError)
    def _connect(self):
        res: Response = get(self.get_url())
        if res.status_code != 200:
            raise exceptions.ConnectionError()

    def get_url(self):
        port = self.get_exposed_port(15672)
        host = self.get_container_host_ip()
        return f"http://{host}:{port}"

    def get_amqp_port(self):
        return self.get_exposed_port(5672)

    def start(self):
        super().start()
        self._connect()
        return self
