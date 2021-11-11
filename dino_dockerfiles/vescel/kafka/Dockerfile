FROM java:8-jre
MAINTAINER mike@cloudmo.de

#install misc utils
RUN apt-get update && \
    apt-get --yes --force-yes install netcat jq net-tools

# Add Consul template
# Releases at https://releases.hashicorp.com/consul-template/
ENV CONSUL_TEMPLATE_VERSION 0.14.0
ENV CONSUL_TEMPLATE_SHA1 7c70ea5f230a70c809333e75fdcff2f6f1e838f29cfb872e1420a63cdf7f3a78

RUN curl --retry 7 -Lso /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \
    && echo "${CONSUL_TEMPLATE_SHA1}  /tmp/consul-template.zip" | sha256sum -c \
    && unzip /tmp/consul-template.zip -d /usr/local/bin \
    && rm /tmp/consul-template.zip

# get ContainerPilot release
ENV CONTAINERPILOT_VERSION=2.1.0

# get Containerpilot release
RUN mkdir -p /opt/containerpilot && \
    curl -k -Lo /tmp/containerpilot.tar.gz https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz && \
    tar xzf /tmp/containerpilot.tar.gz -C /opt/containerpilot/ && \
    rm /tmp/containerpilot.tar.gz
COPY containerpilot.json /etc/

# add ContainerPilot config and tell ContainerPilot where to find it
COPY containerpilot.json /etc/containerpilot.json
ENV CONTAINERPILOT=file:///etc/containerpilot.json

# get Kafka
ENV KAFKA_VERSION=0.9.0.0

LABEL name="kafka" version=$KAFKA_VERSION

RUN wget "http://mirror.cc.columbia.edu/pub/software/apache/kafka/$KAFKA_VERSION/kafka_2.11-$KAFKA_VERSION.tgz" -O /tmp/kafka.tgz \
&& mkdir -p /opt \
&& tar -xvzf /tmp/kafka.tgz -C /opt \
&& mv /opt/kafka_2.11-$KAFKA_VERSION /opt/kafka

WORKDIR /opt/kafka

# copy scripts/default config to image
COPY ./default.server.properties /opt/kafka/config/default.server.properties
COPY ./log4j.properties /opt/kafka/config/log4j.properties
COPY ./manage.sh /opt/kafka/bin/manage.sh

# consul-template files
COPY zkconnect.ctmpl /opt/kafka/config/zkconnect.ctmpl

EXPOSE 9092

CMD ["/opt/containerpilot/containerpilot", "/opt/kafka/bin/manage.sh", "start"]