FROM rabbitmq

COPY ./rabbitmq_stamp-1.0.3.ez /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.4/plugins/rabbitmq_stamp-1.0.3.ez

RUN rabbitmq-plugins enable --offline rabbitmq_management
RUN rabbitmq-plugins enable --offline rabbitmq_stamp
RUN rabbitmq-plugins enable --offline rabbitmq_consistent_hash_exchange

EXPOSE 15671 15672
