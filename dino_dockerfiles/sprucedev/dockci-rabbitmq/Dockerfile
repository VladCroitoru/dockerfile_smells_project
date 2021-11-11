FROM rabbitmq:3.6.0-management

ADD http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_auth_backend_http-3.6.x-3dfe5950.ez /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.0/plugins/
RUN rabbitmq-plugins enable --offline rabbitmq_auth_backend_http
RUN rabbitmq-plugins enable --offline rabbitmq_web_stomp

COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-entrypoint-user.sh /docker-entrypoint-user.sh
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config

EXPOSE 15674

