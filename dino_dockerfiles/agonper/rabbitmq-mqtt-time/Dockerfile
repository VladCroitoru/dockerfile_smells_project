FROM rabbitmq:3.7.3-management

COPY rabbitmq_message_timestamp-20170830-3.7.x.ez /usr/lib/rabbitmq/lib/rabbitmq_server-3.7.3/plugins/

RUN rabbitmq-plugins enable --offline rabbitmq_mqtt
RUN rabbitmq-plugins enable --offline rabbitmq_message_timestamp

# Fix nodename. From cyrilix/rabbit-mqtt
RUN echo 'NODENAME=rabbit@localhost' > /etc/rabbitmq/rabbitmq-env.conf

EXPOSE 1883
