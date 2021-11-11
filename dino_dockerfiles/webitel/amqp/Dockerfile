# vim:set ft=dockerfile:
FROM rabbitmq:3.7-management-alpine
LABEL maintainer="Vitaly Kovalyshyn"

ENV WEBITEL_MAJOR 19
ENV WEBITEL_REPO_BASE https://github.com/webitel

ADD config/ /etc/rabbitmq/
ADD https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip /plugins/
RUN unzip /plugins/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip -d /plugins/ \
    && rm /plugins/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
