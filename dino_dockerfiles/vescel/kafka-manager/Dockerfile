FROM centos:7

MAINTAINER mike@cloudmo.de

RUN yum update -y && \
    yum install -y git wget unzip which && \
    yum clean all

ENV JAVA_MAJOR=8 \
    JAVA_UPDATE=92 \
    JAVA_BUILD=14 

RUN wget -nv --no-cookies --no-check-certificate \
    --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    "http://download.oracle.com/otn-pub/java/jdk/${JAVA_MAJOR}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm" -O /tmp/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm && \
     yum localinstall -y /tmp/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm && \
     rm -f /tmp/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm

ENV JAVA_HOME=/usr/java/jdk1.8.0_${JAVA_UPDATE} \
    ZK_HOSTS=localhost:2181 \
    KM_VERSION=1.3.0.8 \
    KM_REVISION=6e196ea7a332471bead747535f9676f0a2bad008 \
    KM_CONFIGFILE="conf/application.conf"

RUN mkdir -p /tmp && \
    cd /tmp && \
    git clone https://github.com/yahoo/kafka-manager && \
    cd /tmp/kafka-manager && \
    git checkout ${KM_REVISION} && \
    echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt && \
    ./sbt clean dist && \
    unzip  -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \
    rm -fr /tmp/* /root/.sbt /root/.ivy2 && \
    printf '#!/bin/sh\nexec ./bin/kafka-manager -Dconfig.file=${KM_CONFIGFILE} "${KM_ARGS}" "${@}"\n' > /kafka-manager-${KM_VERSION}/km.sh && \
    chmod +x /kafka-manager-${KM_VERSION}/km.sh

# misscellaneous
RUN mkdir -p /opt/kafka-manager && \
    mkdir -p /opt/containerpilot

RUN yum install -y netcat jq iproute

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

# Add Consul template
# Releases at https://releases.hashicorp.com/consul-template/
ENV CONSUL_TEMPLATE_VERSION 0.14.0
ENV CONSUL_TEMPLATE_SHA1 7c70ea5f230a70c809333e75fdcff2f6f1e838f29cfb872e1420a63cdf7f3a78

RUN curl --retry 7 -Lso /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \
    && echo "${CONSUL_TEMPLATE_SHA1}  /tmp/consul-template.zip" | sha256sum -c \
    && unzip /tmp/consul-template.zip -d /usr/local/bin \
    && rm /tmp/consul-template.zip



COPY ./manage.sh /opt/kafka-manager/manage.sh
COPY ./default.application.conf /kafka-manager-${KM_VERSION}/conf/default.application.conf
COPY zkconnect.ctmpl /opt/kafka-manager/conf/zkconnect.ctmpl

WORKDIR /kafka-manager-${KM_VERSION}

EXPOSE 9000


CMD ["/opt/containerpilot/containerpilot", "/opt/kafka-manager/manage.sh", "start"]
