FROM rabbitmq:3.6-management-alpine

RUN apk add --no-cache curl

RUN curl http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_delayed_message_exchange-0.0.1.ez > $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez

RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange rabbitmq_consistent_hash_exchange rabbitmq_shovel rabbitmq_shovel_management

