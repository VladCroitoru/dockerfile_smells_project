FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade system
RUN apk --no-cache upgrade

# Install various tools
RUN apk --no-cache add xz curl jq sudo

# Install RabbitMQ
ENV RABBITMQ_VERSION 3.6.3
ENV RABBITMQ_USER rabbitmq
ENV RABBITMQ_HOME /usr/local/rabbitmq-server
RUN apk --no-cache add erlang erlang-mnesia erlang-public-key erlang-crypto erlang-ssl erlang-sasl \
    erlang-asn1 erlang-inets erlang-os-mon erlang-xmerl erlang-eldap erlang-syntax-tools 
RUN curl -sL https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz | tar -xJ -C /usr/local && \
    ln -s /usr/local/rabbitmq*${RABBITMQ_VERSION} ${RABBITMQ_HOME} 
RUN curl -sL  https://github.com/aweber/rabbitmq-autocluster/releases/download/0.6.1/autocluster-0.6.1.tgz | tar -xz -C ${RABBITMQ_HOME}
RUN adduser -D -s /bin/sh ${RABBITMQ_USER} && chown -R ${RABBITMQ_USER}: /usr/local/rabbitmq*
RUN echo "rabbitmq ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER $RABBITMQ_USER
RUN ${RABBITMQ_HOME}/sbin/rabbitmq-plugins enable --offline autocluster rabbitmq_management rabbitmq_web_stomp
ADD run.sh /
EXPOSE 5671 5672 15672

# Define default command
CMD /run.sh
