FROM rabbitmq:3.5.6
MAINTAINER Dan MacDonald <dsvmacdonald@nuarch.com>

RUN rabbitmq-plugins enable --offline rabbitmq_management rabbitmq_web_stomp rabbitmq_stomp

ADD entrypoint.sh /entrypoint.sh
RUN chmod 755 ./entrypoint.sh

EXPOSE 15672 61613
EXPOSE 5672

CMD ["/entrypoint.sh"]
