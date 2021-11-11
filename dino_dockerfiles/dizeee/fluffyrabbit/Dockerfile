FROM rabbitmq:3.7.2-management-alpine

RUN apk add --update curl && rm -rf /var/cache/apk/*

RUN curl http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_delayed_message_exchange-0.0.1.ez > $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez \
    && rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange

RUN apk del curl

COPY docker-entrypoint-wrapper.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint-wrapper.sh

ENTRYPOINT ["docker-entrypoint-wrapper.sh"]
