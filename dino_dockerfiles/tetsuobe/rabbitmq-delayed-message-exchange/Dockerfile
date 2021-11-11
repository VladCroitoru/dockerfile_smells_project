FROM rabbitmq:3.6-management

RUN apt-get update \
    && apt-get install -y curl --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && curl http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_delayed_message_exchange-0.0.1.ez > $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez \
    && rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange \
    && rabbitmq-plugins enable --offline rabbitmq_consistent_hash_exchange
