#
# Rabbit MQ DockerFile 
#
# https://github.com/dockerfile/rabbitmq
#

# Pull base image.
FROM dockerfile/ubuntu

# Add files.
ADD bin/rabbitmq-start /usr/local/bin/

# Build Env
ENV DEBIAN_FRONTEND noninteractive 
#ENV http_proxy http://192.168.10.1:8080
#ENV ftp_proxy http://192.168.10.1:8080

# Prod Env
ENV RABBITMQ_LOG_BASE /data/log
ENV RABBITMQ_MNESIA_BASE /data/mnesia

# Install RabbitMQ.
RUN \
  wget -qO - www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add - && \
  wget -qO - http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add - && \
  echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list && \
  tail /etc/apt/sources.list.d/rabbitmq.list && \
  apt-get update && \
  apt-get install -y rabbitmq-server && \
  rm -rf /var/lib/apt/lists/*

# Enable RabbitMQ plugins 
RUN \
  rabbitmq-plugins enable rabbitmq_management && \
  rabbitmq-plugins enable rabbitmq_web_stomp && \
  rabbitmq-plugins enable rabbitmq_web_stomp_examples

# Config RabbitMQ
RUN \
  echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config && \
  chmod +x /usr/local/bin/rabbitmq-start

# Define mount points.
VOLUME ["/data/log", "/data/mnesia"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["rabbitmq-start"]

# Expose ports.
EXPOSE 5672
EXPOSE 61613
EXPOSE 15674
EXPOSE 15672
EXPOSE 15670
