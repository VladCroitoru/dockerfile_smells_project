FROM java:8

MAINTAINER Martin Soto <donsoto@gmail.com>

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
       software-properties-common \
       maven \
    && cd /tmp \
    && git clone https://github.com/DeemOpen/zkui.git \
    && cd /tmp/zkui \
    && mvn clean install \
    && mkdir -p /zkui \
    && cp /tmp/zkui/target/zkui-2.0-SNAPSHOT-jar-with-dependencies.jar /zkui \
    && rm -rf /tmp/* /root/.m2 \
    && DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y \
       software-properties-common \
       maven \
    && apt-get autoremove -y \
    && apt-get clean

EXPOSE 9090

ADD config.cfg.template /
ADD start-zkui.sh /usr/bin/
CMD start-zkui.sh
