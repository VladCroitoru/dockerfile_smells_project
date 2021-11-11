FROM openshift/base-centos7

MAINTAINER Stefan Nuxoll <Stefan.Nuxoll@vituity.com>

# Create rabbit user in advance so we have a consistent UID
RUN useradd -r -d /var/lib/rabbitmq -m -U rabbitmq
# Set package versions
ENV RABBITMQ_VERSION 3.7.3
ENV ERLANG_RELEASE_VERSION 1.0-1
# Install Erlang + EPEL repositories
RUN yum install -y https://packages.erlang-solutions.com/erlang-solutions-${ERLANG_RELEASE_VERSION}.noarch.rpm epel-release && yum clean all
# Install RabbitMQ
RUN yum install -y https://github.com/rabbitmq/rabbitmq-server/releases/download/v${RABBITMQ_VERSION}/rabbitmq-server-${RABBITMQ_VERSION}-1.el7.noarch.rpm && yum clean all

# RabbitMQ setup
ENV LANG=en_US.UTF8
ENV RABBITMQ_LOGS=- RABBITMQ_SASL_LOGS=- HOME=/var/lib/rabbitmq
RUN mkdir -p /var/lib/rabbitmq /etc/rabbitmq \
        && touch /etc/rabbitmq/rabbitmq.config \
	&& chown -R rabbitmq:0 /var/lib/rabbitmq /etc/rabbitmq /var/log/rabbitmq \
        && chmod 770 /var/lib/rabbitmq /etc/rabbitmq /var/log/rabbitmq \
        && chmod 660 /etc/rabbitmq/rabbitmq.config \
        && chown rabbitmq:0 /opt/app-root
RUN echo "[{rabbit,[{loopback_users,[]}]}]." >> /etc/rabbitmq/rabbitmq.config
RUN rm -rf /var/lib/rabbitmq/mnesia
RUN /usr/sbin/rabbitmq-plugins enable --offline rabbitmq_management

# Setup volume
VOLUME /var/lib/rabbitmq

# Copy entrypoint script
COPY ./docker-entrypoint.sh /usr/local/bin/

# Tell OpenShift we support random UID's
USER 1001
# Expose ports
EXPOSE 4369 5671 5672 25672 15671 15672
# Set entrypoint and default command
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["rabbitmq-server"]
