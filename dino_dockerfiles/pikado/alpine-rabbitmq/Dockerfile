FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade system
RUN apk --no-cache upgrade

# Install various tools
RUN apk --no-cache add xz curl

# Install RabbitMQ
ENV RABBITMQ_VERSION 3.6.2
ENV RABBITMQ_USER rabbitmq
ENV RABBITMQ_HOME /usr/local/rabbitmq-server
RUN apk --no-cache add erlang erlang-mnesia erlang-public-key erlang-crypto erlang-ssl erlang-sasl \
    erlang-asn1 erlang-inets erlang-os-mon erlang-xmerl erlang-eldap erlang-syntax-tools 
RUN curl -sL https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz | tar -xJ -C /usr/local && \
    ln -s /usr/local/rabbitmq*${RABBITMQ_VERSION} ${RABBITMQ_HOME} && adduser -D -s /bin/sh ${RABBITMQ_USER} && chown -R ${RABBITMQ_USER}: /usr/local/rabbitmq*
USER ${RABBITMQ_USER}
RUN ${RABBITMQ_HOME}/sbin/rabbitmq-plugins enable --offline rabbitmq_management
COPY run.sh /

# Define default command
CMD /run.sh
EXPOSE 5672 15672
