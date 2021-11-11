FROM java:7-jre

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

# install zookeeper
ENV ZOOKEEPER_VER 3.4.8

RUN mkdir -p /opt && \
    wget -q -O - http://apache.mirrors.pair.com/zookeeper/zookeeper-${ZOOKEEPER_VER}/zookeeper-${ZOOKEEPER_VER}.tar.gz | tar -xzf - -C /opt && \
    mv /opt/zookeeper-${ZOOKEEPER_VER} /opt/zookeeper && \
    rm /opt/zookeeper/conf/zoo_sample.cfg && \
    mkdir -p /tmp/zookeeper 


EXPOSE 2181 2888 3888

WORKDIR /opt/zookeeper

VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]

# get ContainerPilot release
ENV CONTAINERPILOT_VERSION=2.0.1

# get Containerpilot release
RUN mkdir -p /opt/containerpilot && \
    curl -k -Lo /tmp/containerpilot.tar.gz https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz && \
    tar xzf /tmp/containerpilot.tar.gz -C /opt/containerpilot/ && \
    rm /tmp/containerpilot.tar.gz
COPY containerpilot.json /etc/

# add ContainerPilot config and tell ContainerPilot where to find it
COPY containerpilot.json /etc/containerpilot.json
ENV CONTAINERPILOT=file:///etc/containerpilot.json

# setup zoo.cfg
COPY zoo.cfg /opt/zookeeper/conf/default.zoo.cfg
COPY zoo.cfg.ctmpl /opt/zookeeper/zoo.cfg.ctmpl
COPY manage.sh /opt/zookeeper/manage.sh


CMD ["/opt/containerpilot/containerpilot", "/opt/zookeeper/manage.sh", "start"]