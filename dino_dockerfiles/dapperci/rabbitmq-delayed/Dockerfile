FROM maryville/rabbitmq:3.6.6

RUN wget http://dl.bintray.com/rabbitmq/community-plugins/rabbitmq_delayed_message_exchange-0.0.1.ez -O $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez && \
    rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange
