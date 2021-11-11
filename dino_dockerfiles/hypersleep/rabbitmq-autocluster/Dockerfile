FROM rabbitmq:3.5.5-management

RUN curl -o /usr/lib/rabbitmq/lib/rabbitmq_server-3.5.5/plugins/autocluster-0.4.1.ez -SL https://github.com/aweber/rabbitmq-autocluster/releases/download/0.4.1/autocluster-0.4.1.ez

ENV AUTOCLUSTER_TYPE consul

RUN rabbitmq-plugins enable autocluster


