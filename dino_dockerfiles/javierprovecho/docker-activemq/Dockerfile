FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    wget \
    default-jdk \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/* \
&&  wget -qO- http://apache.rediris.es/activemq/5.13.0/apache-activemq-5.13.0-bin.tar.gz \
|   tar zxv -C /root \
&&  /root/apache-activemq-5.13.0/bin/activemq create /opt/activemq

COPY . /
EXPOSE 8161 61616 5672 61613 1883 61614

ENTRYPOINT ["/bin/sh"]
CMD ["/run.sh"]
