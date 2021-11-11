FROM rabbitmq:3.6.0

RUN rabbitmq-plugins enable --offline rabbitmq_web_stomp
RUN rabbitmq-plugins enable --offline rabbitmq_management

RUN service rabbitmq-server restart

EXPOSE 15674