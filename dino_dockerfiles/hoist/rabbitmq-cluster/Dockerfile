FROM totem/python-base:3.4-trusty-b2

ENV DEBIAN_FRONTEND noninteractive

#Install Supervisor
RUN pip install supervisor==3.1.2 supervisor-stdout


# Install RabbitMQ.
RUN \
  wget -qO - http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add - && \
  wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_5_7/rabbitmq-server_3.5.7-1_all.deb && \
  echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list && \
  apt-get update && \
  sudo dpkg -i rabbitmq-server_3.5.7-1_all.deb || true && \
  DEBIAN_FRONTEND=noninteractive sudo apt-get install -f -y && \
  apt-get clean && \
  rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
  rabbitmq-plugins enable rabbitmq_management && \
  echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config

#Install delayed message exchange plugin
RUN curl -L http://www.rabbitmq.com/community-plugins/v3.5.x/rabbitmq_delayed_message_exchange-0.0.1-rmq3.5.x-9bf265e4.ez -o /usr/lib/rabbitmq/lib/rabbitmq_server-3.5.7/plugins/rabbitmq_delayed_message_exchange.ez && rabbitmq-plugins enable rabbitmq_delayed_message_exchange

#Confd
ENV CONFD_VERSION 0.6.2
RUN curl -L https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-${CONFD_VERSION}-linux-amd64 -o /usr/local/bin/confd && \
    chmod 555 /usr/local/bin/confd

#Etcdctl
ENV ETCDCTL_VERSION v0.4.6
RUN curl -L https://github.com/coreos/etcd/releases/download/$ETCDCTL_VERSION/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz -o /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz && \
    cd /tmp && gzip -dc etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz | tar -xof - && \
    cp -f /tmp/etcd-$ETCDCTL_VERSION-linux-amd64/etcdctl /usr/local/bin && \
    rm -rf /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz

#Configure Rabbitmq
RUN sed --follow-symlinks \
    -e 's/-rabbit error_logger.*/-rabbit error_logger tty \\/' \
    -e 's/-rabbit sasl_error_logger.*/-rabbit sasl_error_logger tty \\/' \
    -e 's/-sasl sasl_error_logger.*/-sasl sasl_error_logger tty \\/' \
    -i  /usr/lib/rabbitmq/bin/rabbitmq-server

#Supervisor Config
RUN mkdir -p /var/log/supervisor
ADD etc/supervisor /etc/supervisor
RUN ln -sf /etc/supervisor/supervisord.conf /etc/supervisord.conf

#Confd Defaults
ADD etc/confd /etc/confd

#Add custom scipts
ADD bin /usr/local/bin
RUN chmod -R +x /usr/local/bin

# Define mount points.
VOLUME ["/var/lib/rabbitmq"]

EXPOSE 5672 44001 15672 25672 4369

ENTRYPOINT ["/usr/local/bin/supervisord-wrapper.sh"]
