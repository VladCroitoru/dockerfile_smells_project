FROM dockerfile/ubuntu
MAINTAINER Namhoon (emerald105@hanmail.net)

ENV DEBIAN_FRONTEND noninteractive

# Install RabbitMQ
RUN \
  wget -qO - http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add - && \
  echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list && \
  apt-get update && \
  apt-get install -y rabbitmq-server && \
  rm -rf /var/lib/apt/lists/* && \
  rabbitmq-plugins enable rabbitmq_management && \
  echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config

ENV RABBITMQ_LOG_BASE /data/log
ENV RABBITMQ_MNESIA_BASE /data/mnesia
ENV RABBITMQ_NODE_PORT 8510

ADD ./start.sh /start.sh
RUN chmod +x /start.sh

VOLUME ["/data/log", "/data/mnesia"]

# Run
WORKDIR /root
CMD ["/start.sh"]

# Expose rabbitmq node port
EXPOSE 8510
# Expose web management http port
EXPOSE 15672
