FROM dockerfile/java:oracle-java8

ADD https://www.rabbitmq.com/releases/rabbitmq-java-client/v3.3.5/rabbitmq-java-client-bin-3.3.5.tar.gz /data/client.tar.gz
WORKDIR /data
RUN tar -zvvxf /data/client.tar.gz
RUN mv /data/rabbitmq-java-* /data/client

ADD start.sh /data/start.sh

ENTRYPOINT ["/data/start.sh"]

