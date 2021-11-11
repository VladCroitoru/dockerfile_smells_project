FROM rabbitmq:3.6.3-management

COPY rabbitmq.config /etc/rabbitmq/
COPY custom_definitions.json /etc/rabbitmq/
CMD ["rabbitmq-server"]
