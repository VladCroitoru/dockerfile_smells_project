FROM dockerfile/java:oracle-java7

# Update packages
RUN apt-get update

RUN wget -q http://www.us.apache.org/dist/kafka/0.8.1.1/kafka_2.10-0.8.1.1.tgz -O /tmp/kafka_2.10-0.8.1.1.tgz
RUN tar xfz /tmp/kafka_2.10-0.8.1.1.tgz -C /opt

VOLUME ["/data"]

ADD server.properties /etc/kafka/server.properties

CMD ["/opt/kafka_2.10-0.8.1.1/bin/kafka-server-start.sh", "/etc/kafka/server.properties"]
