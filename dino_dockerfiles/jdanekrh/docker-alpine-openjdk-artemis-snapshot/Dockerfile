#
# Alpine Linux - AMQ7 snapshot Dockerfile
#

FROM library/fedora:27

MAINTAINER Jiri Danek <jdanek@redhat.com>

USER root

RUN yum install -y \
    java-1.8.0-openjdk \
    libaio \
    patch \
    unzip \
    wget \
    grep \
    && yum clean all

# create artemis user
RUN adduser amq7

# Setup broker
ADD setup_broker.sh ./
RUN ./setup_broker.sh

# Hawtio Managment Console
EXPOSE 8161

# Artemis | CORE,MQTT,AMQP,HORNETQ,STOMP,OPENWIRE
EXPOSE 61616

# AMQP
EXPOSE 5672

# HORNETQ,STOMP
EXPOSE 5445

# MQTT
EXPOSE 1883

# STOMP
EXPOSE 61613

# Expose some outstanding folders
VOLUME ["/var/lib/amq7/data"]
VOLUME ["/var/lib/amq7/tmp"]
VOLUME ["/var/lib/amq7/etc"]

WORKDIR /var/lib/amq7/bin

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["amq7-server"]
